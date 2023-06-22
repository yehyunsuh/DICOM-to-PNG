import pydicom
import numpy as np
import os

from PIL import Image
from glob import glob
from tqdm import tqdm


if not os.path.exists('./png'):        
    os.mkdir('./png')

tmp_dicom_lists = glob('./dicom_files/*')
time, tmp, image, dicom_lists = [], [], [], []

for dicom_list in tmp_dicom_lists:
    time.append(glob(f'{dicom_list}/*'))

for i in range(len(time)):
    for dicom_list in time[i]:
        tmp.append(glob(f'{dicom_list}/*'))

for i in range(len(tmp)):
    for dicom_list in tmp[i]:
        image.append(glob(f'{dicom_list}/*'))

for list in image:
    for dicom_list in list:
        tmp_list = glob(f'{dicom_list}/*')
        for i in range(len(tmp_list)):
            dicom_lists.append(tmp_list[i])
print("Total number of images is: ",len(dicom_lists))

for dicom_name in tqdm(dicom_lists):
    try:
        dcm_info = pydicom.read_file(f'{dicom_name}', force=True)
        dcm_img = dcm_info.pixel_array
        split = dicom_name.split('/')
        file_name = f'{split[-5]}_{split[-4]}_{split[-3]}_{split[-2]}_{split[-1]}'

        norm = (dcm_img - np.min(dcm_img)) / (np.max(dcm_img) - np.min(dcm_img))
        norm_img = np.uint8(norm*255)
        show_img = Image.fromarray(norm_img)
        show_img.save(f'./png/{file_name}.png')
    except: 
        print(f'This file --{dicom_name}-- did not convert to PNG format')