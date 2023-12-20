# Medical Bill Category Classifier

This Flask application is designed to classify medical bill descriptions into different categories based on keywords present in the text. It uses a simple string matching algorithm to match keywords extracted from a dataset to classify the input text.

## Setup and Installation

1. Clone the Repository:

```
git clone https://github.com/your-username/medical-bill-classifier.git
cd medical-bill-classifier
```

2. Install Dependencies:

Ensure you have Python installed. Then, install the required packages:

```
pip install flask pandas openpyxl
```

3. Dataset

Prepare your medical bills dataset in Excel format (.xlsx) with columns Category and Description. Update the file_path variable in app.py to point to your dataset:

```
file_path = './medical_bills.xlsx'
```

# Medical Bill Data Extraction

This Python script facilitates the extraction of structured data from medical bills in PDF format.

## Prerequisites

Ensure you have the following libraries installed:

- PyMuPDF (`fitz`)
- `json`
- `re`
- `pdf2image`
- `easyocr`

Install the dependencies via pip:

```bash
pip install PyMuPDF pdf2image easyocr
```

## Usage

1. Data Extraction from PDF

- Run extract_data_from_bill(pdf_path) to extract data from a medical bill PDF.
- Replace pdf_path with the path to your medical bill PDF.
- Saving Extracted Data to JSON

2. Use save_to_json(data, output_file) to save the extracted data to a JSON file.

- Replace output_file with the desired output JSON file name.
- Extracting Text from Images

3. Process images of the medical bill using OCR to extract textual information.

- Requires pdf2image and easyocr.
- Images will be converted from the PDF pages and stored as JPEG files.
- Modify the image file names in the image_files list to match your image files.
- Structure of Extracted Data

4. Extracted data is organized in JSON format.

- Data includes descriptions and charged amounts from the bill.
- Additional tables and package information extracted from specific pages of the bill are structured within the JSON.

## Important Notes

- Modify regex patterns in extract_data_from_bill() to match your bill's format for accurate extraction.
- Ensure correct paths to PDFs/images are provided.
- Review and customize table structures and extraction logic for different bill formats.
