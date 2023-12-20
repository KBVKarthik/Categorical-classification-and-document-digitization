from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

app = Flask(__name__)

# Load dataset (assuming it's in an Excel file named 'medical_bills.xlsx')
# Replace 'file_path' with the actual path to your Excel dataset
file_path = './medical_bills.xlsx'
data = pd.read_excel(file_path)

# Prepare data
X = data['description']
y = data['category']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train a classifier (using LinearSVC in this example)
classifier = LinearSVC()
classifier.fit(X_vectorized, y)

# Function to classify using the trained model
def classify_with_model(text):
    text_vectorized = vectorizer.transform([text])
    predicted_category = classifier.predict(text_vectorized)
    return predicted_category[0]

# API endpoint to predict category
@app.route('/predict_category', methods=['POST'])
def predict_category():
    content = request.json
    text = content['text']
    
    predicted_category = classify_with_model(text)
    return jsonify({'category': predicted_category})

if __name__ == '__main__':
    app.run(debug=True)