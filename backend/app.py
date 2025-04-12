from flask import Flask, request, jsonify
import joblib
import pytesseract
from PIL import Image
import re
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

model_path = "model/financial_text_classifier.joblib"
model = joblib.load(model_path)

def ocr_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9₹.,:/\s-]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    try:
        raw_text = ocr_from_image(file_path)
        cleaned = clean_text(raw_text)
        prediction = model.predict([cleaned])[0]
        confidence = model.predict_proba([cleaned]).max()

        os.remove(file_path)

        return jsonify({
            'prediction': prediction,
            'confidence': round(float(confidence), 4),
            'extracted_text': raw_text.strip()[:300]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
