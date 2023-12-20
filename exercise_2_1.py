import fitz  # PyMuPDF
import json
import re

def extract_data_from_bill(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Initialize lists to store extracted data
    descriptions = []
    charged_amounts = []

    # Iterate through pages
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")

        # Use regex to find descriptions and charged amounts
        # Customize the regex pattern according to your bill format
        matches = re.findall(r'([A-Za-z\s]+)\n([\d,]+\.\d{2})', text)

        # Adding extracted data to respective lists
        for match in matches:
            description = match[0].strip()
            charged_amount = float(match[1].replace(',', ''))  # Convert amount to float

            descriptions.append(description)
            charged_amounts.append(charged_amount)

    # Close the PDF document
    pdf_document.close()

    # Create a structured dictionary
    data = {"billed_items": []}

    # Add extracted data to the structured dictionary
    for desc, amount in zip(descriptions, charged_amounts):
        data["billed_items"].append({
            "description": desc,
            "charged_amount": amount
        })

    return data

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Replace 'path_to_your_pdf.pdf' with the actual path to your medical bill PDF
pdf_path = 'Exercise_2_Data_1.pdf'

# Extract data from the PDF
extracted_data = extract_data_from_bill(pdf_path)

# Save the extracted data to a JSON file
output_json_file = 'exercise_2_1.json'
save_to_json(extracted_data, output_json_file)
