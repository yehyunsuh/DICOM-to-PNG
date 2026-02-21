# Converting DICOM to PNG

## Prerequisites

### Python 3
- If you already have Python 3 installed, you do not need to install it again.
- If you do not have Python 3, download it from https://www.python.org/downloads/

### Install dependencies
Run in your terminal:
```shell
pip3 install pydicom numpy pillow tqdm
```

## 1. Folder setup

Place your DICOM files under the `dicom_files` directory (or another folder and pass it via `--dicom_folder`):

```
DICOM-to-PNG
├── dicom_files          ← DICOM files go here (any subfolder structure)
├── png                   ← Converted PNGs are written here
└── dicom_to_png.py
```

## 2. Running the script

From the project folder, run:

```shell
cd <<path to DICOM-to-PNG folder>>
python3 dicom_to_png.py
```

**Optional arguments:**
- `--dicom_folder` — Folder to search for DICOM files (default: `dicom_files`)
- `--png_folder` — Folder where PNG files are saved (default: `png`)

Example with custom folders:
```shell
python3 dicom_to_png.py --dicom_folder my_dicoms --png_folder my_pngs
```

## 3. Which files are converted

Only **actual DICOM files** are converted. The script detects DICOM by checking for the standard DICOM file signature (the 4-byte `"DICM"` marker at offset 128). Other files in the same tree (e.g. `README.TXT`, `DICOMDIR`, `CONTENT.XML`) are ignored and are not attempted for conversion.

## 4. Output layout

Converted PNGs are saved under the `png` folder (or the folder set by `--png_folder`):

```
DICOM-to-PNG
├── dicom_files
├── png                   ← All converted PNG files
└── dicom_to_png.py
```

## 5. PNG file naming

Each PNG filename is derived from the path of the source DICOM file:

- Path segments are joined with underscores.
- The segment named **DICOM** (any case) is **omitted** from the filename.
- The final filename is **lowercase**.

**Example**

If the DICOM file path is:
```
dicom_files/4681433/FollowUp/DICOM/0000B7F3_AA5E6319_AA1989FA_0000D4DA_EEF1C181
```

The PNG filename will be:
```
4681433_followup_0000b7f3_aa5e6319_aa1989fa_0000d4da_eef1c181.png
```

Another example:
```
dicom_files/AAAAA/BBBBB/CCCCC/DDDDD.dcm
```
→ PNG name: `aaaaa_bbbbb_ccccc_ddddd.png`
