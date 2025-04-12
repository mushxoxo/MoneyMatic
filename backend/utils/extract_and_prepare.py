import os
import pytesseract
from PIL import Image
import pandas as pd
import re

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

BASE_DIR = "./dataset"
ocr_data = []

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(root, file)
            try:
                img = Image.open(filepath)
                text = pytesseract.image_to_string(img)

                ocr_data.append({
                    "folder": os.path.basename(root),
                    "filename": file,
                    "filepath": filepath,
                    "raw_text": text
                })
                print(f"✅ OCR complete for {filepath}")
            except Exception as e:
                print(f"❌ Error processing {filepath}: {e}")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9₹.,:/\s-]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df = pd.DataFrame(ocr_data)
df['clean_text'] = df['raw_text'].apply(clean_text)

df['label'] = df['folder']  


df.to_csv("cleaned_financial_text_data.csv", index=False)
print("\n📁 All OCR and preprocessing complete. Saved to cleaned_financial_text_data.csv")
