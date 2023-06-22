import pydicom
import numpy as np
import os

from PIL import Image
from tdqm import tdqm


if not os.path.exists('./png'):        
    os.mkdir('./png')

dicom_list = os.listdir('./dicom_files')
for dicom_name in dicom_list:
    try: 
        dcm_info = pydicom.read_file(f'./dicom_files/{dicom_name}', force=True)
        dcm_img = dcm_info.pixel_array

        norm = (dcm_img - np.min(dcm_img)) / (np.max(dcm_img) - np.min(dcm_img))
        norm_img = np.uint8(norm*255)
        show_img = Image.fromarray(norm_img)
        show_img.save(f'./png/{dicom_name}.png')
    except:
        print(f'This file --{dicom_name}-- did not convert to PNG format')