import re
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

def generate_category_keywords(data):
    categories = {}
    for index, row in data.iterrows():
        category = row['category']
        text = row['description']
        if category not in categories:
            categories[category] = set()
        keywords = text.lower().split()
        categories[category].update(keywords)
    return categories

# Load dataset from Excel
file_path = './medical_bills.xlsx'
data = pd.read_excel(file_path)

# Generate category keywords dictionary
category_keywords = generate_category_keywords(data)

def classify_string_matching(text):
    text_lower = text.lower()
    
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            pattern = r'\b{}\b'.format(re.escape(keyword))
            if re.search(pattern, text_lower):
                return category
    
    return 'Unclassified'

@app.route('/classify', methods=['POST'])
def classify():
    input_text = request.json.get('text', '')
    category = classify_string_matching(input_text)
    return jsonify({'category': category})

if __name__ == '__main__':
    app.run(debug=True)