import numpy as np
import pydicom
import argparse
import os

from PIL import Image
from glob import glob
from tqdm import tqdm


def main(args):
    path_list, dicom_path_list = [], []
    path_list.append(args.dicom_folder)

    # Create png folder
    os.makedirs(args.png_folder, exist_ok=True)

    # Search for path to all dicom files
    while path_list != []:
        current_path = path_list.pop()
        tmp_path_list = glob(f'{current_path}/*')

        if tmp_path_list != []:
            for tmp_path in tmp_path_list:
                path_list.append(tmp_path)
        else:
            dicom_path_list.append(current_path)

    # From the paths found, convert them in to png format
    for dicom_name in tqdm(dicom_path_list):
        try:
            dcm_info = pydicom.read_file(f'{dicom_name}', force=True)
            dcm_img = dcm_info.pixel_array
            split = dicom_name.split('/')
            file_name = f'{split[1]}'

            for i in range(2, len(split)):
                if split[i] == args.dicom_folder:
                    break
                file_name += f'_{split[i]}'

            norm = (dcm_img-np.min(dcm_img))/(np.max(dcm_img)-np.min(dcm_img))
            norm_img = np.uint8(norm*255)
            show_img = Image.fromarray(norm_img)
            show_img.save(f'{args.png_folder}/{file_name}.png')
        except:
            print(f'This file {dicom_name} did not convert to PNG format')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dicom_folder', type=str, default="dicom_files")
    parser.add_argument('--png_folder', type=str, default="png")
    args = parser.parse_args()

    main(args)
