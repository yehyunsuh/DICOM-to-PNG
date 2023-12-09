# Converting Dicom to PNG
## Prerequisites
### Python3
- If you already have downloaded python3 before, you do not have to download it again   
- If you do not have python3 installed, go to the link below and download python3 https://www.python.org/downloads/

### Download libraries
- Type the following in your `terminal`
```shell
pip3 install pydicom numpy pillow tqdm argparse
```
## 1. How to set up your folders
```
Dicom
├─ dicom_files
|   └─ here goes the dicom files
└─ dicom_to_png.py
```
## 2. Run python file
- Type the following in your `terminal`
```python3
cd <<path to Dicom folder>>
python3 dicom_to_png.py
```

## 3. How it should look like after creating PNG files
- All the DICOM files converted to PNG will be saved in `png` folder
```
Dicom
├─ dicom_files
├─ png
└─ dicom_to_png.py
```

## 4. PNG file name
Your PNG file name will be
```
<<path to dicom file>>_<<name of dicom file>>.png
```
For example, 
```
dicom_files/AAAAA/BBBBB/CCCCC/DDDDD/EEEEE/dicom.dcm
```
if your dicom file was in path, your name of your dicom file will be
```
AAAAA_BBBBB_CCCCC_DDDDD_EEEEE_dicom.png
```
