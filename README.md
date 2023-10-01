# Timetable-PDF-Export

Extract timetable information from PDFs and export them to a json format that can be used in [my-public-transit](https://dev-mbo.github.io).

## ! work_in_progress ! 

## Setup:
Create `venv`:
```
virtualenv venv
```

Prerequistes:

Install [Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for text extraction from images. PDF2image also requires `poppler` as a pdf rendering library. See [here](https://pypi.org/project/pdf2image/) for more information.  

Install requirements:
```
pip3 install -r requirements.txt
``` 

## Usage:
Run the script via 
```
python3 src/main.py [path_to_pdf_file]
```