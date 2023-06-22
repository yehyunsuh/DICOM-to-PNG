# Dealing with DICOM files

## Prerequisites
### Python3
- If you already have downloaded python3 before, you do not have to download it again   
- If you do not have python3 installed, go to the link below and download python3 https://www.python.org/downloads/

### Download libraries
- Type the following in your `terminal`
```shell
pip3 install pydicom numpy pillow tqdm opencv-python argparse
```

# Convert Dicom to PNG
## 1. When you have all the dicom files in one folder
### 1.1 How to set up your folders
```
Dicom
├─ dicom_files
|   └─ here goes the dicom files
└─ dicom_to_png1.py
```
### 1.2 Run python file
- Type the following in your `terminal`
```python3
cd <<path to Dicom folder>>
python3 dicom_to_png1.py
```

## 2. When you have dicom files in raw format
### 2.1 How to set up your folders
```
Dicom
├─ dicom_files
|   └─ Directory 1
|       └─ Directory 2
|           └─ Directory 3
|               └─ Directory 4
|                   └─ here goes the dicom files
└─ dicom_to_png2.py
```
### 2.2 Run python file
- Type the following in your `terminal`
```python3
cd <<path to Dicom folder>>
python3 dicom_to_png2.py
```

## 3. How it should look like after creating PNG files
- All the DICOM files converted to PNG will be saved in `png` folder
```
Dicom
├─ dicom_files
├─ png
└─ dicom_to_png.py
```

# Annotating the Markers (Labeling the Image)
## 1. When you have PNG files in `png` folder
### 1.1 How the folder should look like
```
Dicom
├─ dicom_files
├─ png
├─ dicom_to_png.py
└─ marker_annotator.py
```
### 1.2 Run python file
- Type the following in your `terminal`
```python3
cd <<path to Dicom folder>>
python3 marker_annotator.py
```

## 2. When you have PNG files in other folder
### 2.1 How the folder should look like
```
Dicom
├─ dicom_files
├─ <<name of the png folder>>
├─ dicom_to_png.py
└─ marker_annotator.py
```
### 2.2 Run python file
- Type the following in your `terminal`
```python3
cd <<path to Dicom folder>>
python3 marker_annotator.py --path <<name of the png folder>>
```

## 3. How to annotate the markers
- `left click`: every time you do a click, there will be a red dot generated in the image and coordinates of the red dot will be extracted
- `b`: when you annotate the wrong point, press `b` and the dot will be erased
- `n`: when you are done with one image, press `n` and you can move on to the next image
- `q`: when you are done with annotating, press `q` and program will be terminated
- After executing the file, you will have a txt file that has `current date + current time + folder name.txt`