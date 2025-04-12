import joblib
import pytesseract
from PIL import Image
import re
import sys
import os

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

model = joblib.load("model/financial_text_classifier.joblib")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9₹.,:/\s-]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def ocr_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def predict_category(input_data):
    cleaned = clean_text(input_data)
    prediction = model.predict([cleaned])[0]
    return prediction

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("⚠️ Usage: python predict.py <image_path or raw_text>")
        sys.exit(1)

    arg = sys.argv[1]

    if os.path.isfile(arg) and arg.lower().endswith(('.jpg', '.jpeg', '.png')):
        extracted_text = ocr_image(arg)
        predicted = predict_category(extracted_text)
        print(f"\n📷 Extracted Text:\n{extracted_text.strip()[:300]}...\n")
        print(f"🔮 Predicted Category: {predicted}")

    else:
        predicted = predict_category(arg)
        print(f"🔮 Predicted Category: {predicted}")
