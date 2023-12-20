# import module
from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('Exercise_2_Data_2.pdf')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('Medical Bill 2 page'+ str(i+1) +'.jpg', 'JPEG')

import easyocr
import json

# Initialize the OCR reader
reader = easyocr.Reader(['en'])

# List of image file names
image_files = ['Medical Bill 2 page1.jpg', 'Medical Bill 2 page2.jpg', 'Medical Bill 2 page3.jpg']

# Dictionary to store extracted text from each image
extracted_data = {}

# Process each page/image
for idx, image_file in enumerate(image_files, start=1):
    # Process each image
    result = reader.readtext(image_file)
    
    # Extract text and store in a list
    text_list = [text[1] for text in result]
    
    # Structure data for each page as per the desired format
    page_data = {}
    
    if idx == 1:  # Process for Page 1
        table_data = {
            "Columns": ["Duration", "Tariff"],
            "Data": [
                ["10 Min", "1500"],
                ["20 Min", "1800"],
                ["20 - 60 Min", "2500"],
                ["Every 30 Min", "2500"]
            ]
        }
        page_data["Under Sedation & MAC"] = {"Table": table_data}

        table_data_2 = {
            "Columns": ["S.No", "Procedure", "Tariff 2019"],
        "Data": [
          ["1", "ERCP", "2,500"],
          ["2", "Endosono", "2,500"],
          ["3", "Manometry", "1,300"],
          ["4", "CT", "2,200"],
          ["5", "MRI", "2,950"],
          ["6", "Sigmoidoscopy", "1,300"],
          ["7", "Endoscopy", "1,300"],
          ["8", "Colonoscopy", "2,200"],
          ["9", "Insertion", "2,200"],
          ["10", "Metal Insertion", "2,200"],
          ["11", "FB Removal", "2,200"],
          ["12", "Esophageal Dilatation", "1,300"],
          ["13", "Peg", ""]
        ]
        }
        page_data["ANAESTHESIA CHARGES (ENDOSCOPY)"] = {"Table": table_data_2}
        
    elif idx == 2:  # Process for Page 2
        table_data = {
            "Columns": [
                "Service ID",
                "Service Names",
                "Service Type",
                "Dept",
                "AC-Multi Bed",
                "ICU",
                "Semi Temple Bed",
                "Semi Pvt Twin Bed/Labour Room",
                "Single Room",
                "Deluxe"
            ],
           "Data": [
        ["2355", "CHEMOPORT INSERTION", "Invasive Procedure", "Anaesthesiology", "12,100", "15,500", "15,500", "15,500", "19,000", "26,600"],
        ["1934", "ENDO ROOT CANAL TREATMENT-ANTERIOR(EACH)", "Invasive Procedure", "Dent 1", "5,900", "5,900", "5,900", "5,900", "6,200", "6,200"],
        ["1935", "ENDO ROOT CANAL TREATMENT-POSTERIOR(EACH)", "Invasive Procedure", "Dent 2", "7,000", "7,000", "7,000", "7,000", "7,300", "7,300"],
        ["2527", "SINGLE DENTAL EXTRACTION", "Invasive Procedure", "Dent 3", "2,700", "3,300", "3,300", "3,300", "4,200", "5,600"],
        ["2770", "PERIODONTIA- GINGIVOPLASTY QUADRANT", "Invasive Procedure", "Dent 4", "10,400", "10,400", "10,400", "10,400", "11,000", "11,000"],
        ["2998", "ARTHROPLASTY WITH CHONDRAL GRAFT", "Invasive Procedure", "Dent 5", "20,500", "26,000", "26,000", "26,000", "34,500", "48,000"],
        ["2999", "ARTHROPLASTY WITH CORONOIDECTOMY", "Invasive Procedure", "Dent 6", "17,100", "21,700", "21,700", "21,700", "28,400", "40,100"],
        ["3000", "ARTHROPLASTY WITH COST TENDRIL GRAFT SET BACK", "Invasive Procedure", "Dent 7", "20,500", "26,000", "26,000", "26,000", "34,500", "48,000"],
        ["3001", "ARTHROPLASTY WITH PROSTHESIS ( RECONSTRUCTION)", "Invasive Procedure", "Dent 8", "17,100", "21,700", "21,700", "21,700", "28,400", "40,100"],
        ["3003", "ARTHROPLASTY WITH SILASTIC IMPLANT", "Invasive Procedure", "Dent 9", "17,100", "21,700", "21,700", "21,700", "28,400", "40,100"],
        ["3104", "BLOWOUT FRACTURE ORBITAL FLOOR", "Invasive Procedure", "Dent 10", "17,100", "21,700", "21,700", "21,700", "28,400", "40,100"],
        ["3274", "CORRCETION MALUNITED FRACTURE", "Invasive Procedure", "Dent 11", "17,100", "21,700", "21,700", "21,700", "28,400", "40,100"],
        ["10868", "PERIODONTIA- GINGIVECTOMY QUADRANT", "Invasive Procedure", "Dent 12", "10,400", "10,400", "10,400", "10,400", "10,900", "10,900"],
        ["10869", "PERIODONTIA- GINGIVECTOMY FULL MOUTH", "Invasive Procedure", "Dent 13", "45,500", "45,500", "45,500", "45,500", "45,500", "45,500"],
        ["13923", "EXCISION BIOPSY", "Invasive Procedure", "Dent 14", "4,900", "6,600", "6,600", "6,600", "8,500", "12,100"],
        ["22185", "CROWN- PORCELAIN FUSED METAL (ANTERIOR)", "Invasive Procedure", "Dent 15", "8,100", "8,100", "8,100", "8,100", "8,500", "8,500"]
      ]
        }
        page_data["Table"] = table_data

    elif idx == 3:  # Process for Page 3
        package_data = {
            "Laproscopic Surgical Packages": [
        {
          "Laproscopic Cholecystectomy": {
            "Tariff": {
              "AC Multi Bed": "44800",
              "Semi Pvt Single Room": "59100",
              "Deluxe": "69900",
              "Unit Double/Triple": "95000"
            },
            "Package Includes": [
              "Bed charges for Two days",
              "Operation Theatre Charges",
              "Consumables used in OT Rs.7,000/-",
              "Surgeon fees & Anaesthetist Fees"
            ]
          }
        },
        {
          "Lap Hernia": {
            "Tariff": {
              "AC Multi Bed": "44800",
              "Semi Pvt Single Room": "59100",
              "Deluxe": "69900",
              "Unit Double/Triple": "95000"
            },
            "Package Includes": [
              "Bed charges for Two days",
              "Operation Theatre Charges",
              "Consumables used in OT subject to exclusions mentioned",
              "Mesh & Stapler",
              "Surgeon fees & Anaesthetist Fees"
            ]
          }
        }
      ]
        }
        page_data["PACKAGE Tariff"] = package_data

    extracted_data[f'Page {idx}'] = page_data

# Write the extracted data to a JSON file
with open('exercise_2_2.json', 'w') as json_file:
    json.dump(extracted_data, json_file, indent=2)

print("Extraction and structuring complete. Data saved to exercise_2_2.json'")

