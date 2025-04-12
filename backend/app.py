import joblib
import pytesseract
from PIL import Image
import re
import os

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# Load trained model
model_path = "model/financial_text_classifier.joblib"
model = joblib.load(model_path)

# OCR function
def ocr_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Clean text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9₹.,:/\s-]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

if __name__ == "__main__":
    # Path to sample image
    image_path = "sample.jpg"

    if not os.path.exists(image_path):
        print(f"❌ Image not found at {image_path}")
        print("👉 Please place your sample image as 'sample.jpg'")
        exit()

    print("🔍 Extracting text from image...")
    raw_text = ocr_from_image(image_path)

    print("\n📄 Extracted Text Preview:")
    print(raw_text.strip()[:300])

    cleaned = clean_text(raw_text)
    prediction = model.predict([cleaned])[0]
    confidence = model.predict_proba([cleaned]).max()

    print("\n✅ Prediction:")
    print(f"Category: {prediction}")
    print(f"Confidence: {round(float(confidence), 4)}")
