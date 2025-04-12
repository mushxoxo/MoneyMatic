import os
import pytesseract
from PIL import Image
import pandas as pd
import re

# Step 1: Set up Tesseract if needed (optional)
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# Step 2: OCR extraction from nested folders
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

# Step 3: Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9₹.,:/\s-]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Step 4: Convert to DataFrame
df = pd.DataFrame(ocr_data)
df['clean_text'] = df['raw_text'].apply(clean_text)

# Step 5: Add placeholder label (optional)
# You can edit this CSV later to manually assign true labels
df['label'] = df['folder']  # Use folder name as initial label

# Step 6: Save to CSV
df.to_csv("cleaned_financial_text_data.csv", index=False)
print("\n📁 All OCR and preprocessing complete. Saved to cleaned_financial_text_data.csv")
