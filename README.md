
# 💸 MoneyMatic

This project is a Flask-based web application that lets you upload scanned financial documents (images) and classifies them into categories like:

- Balance Sheets  
- Cash Flow  
- Income Statement  
- Notes  
- Others  

It uses:

- OCR (pytesseract) to extract text from images  
- spaCy for preprocessing  
- Gensim Word2Vec embeddings  
- TensorFlow CNN model for classification  

—

🚀 Features

- Upload a .jpg/.png image from your browser  
- Automatically extracts and processes text  
- Predicts financial document type  
- Displays confidence score and extracted text preview  

—

📦 Requirements

Install Python 3.8+ and the required packages:

pip install -r requirements.txt

Also install Tesseract OCR engine:

- Windows: https://github.com/tesseract-ocr/tesseract  
- Ubuntu: sudo apt install tesseract-ocr  
- Mac (brew): brew install tesseract  

—

▶️ How to Run

1. Start the Flask app:

python app.py

2. Visit the web app:

http://localhost:5000

3. Upload a scanned financial image and view predictions

—

🧪 Example Output

{
  "prediction": "Income Statement",
  "confidence": 94.23,
  "text": "Revenue for the quarter ended March 2024 was ₹120 Cr..."
}

—

🧰 Model Training (optional)

If you're training your own models:

- Preprocess and label your text data  
- Train Word2Vec using gensim  
- Extract embeddings and train a 1D CNN using TensorFlow/Keras  

—

📌 Notes

- Make sure punkt is downloaded by nltk:

  import nltk  
  nltk.download('punkt')

- Model expects 300-dim embeddings by default  
- You can extend it to support PDF, multi-page, and streamlit frontend easily  
