
# 💸 MoneyMatic

**MoneyMatic** is an AI-powered web application that extracts and classifies scanned financial documents using OCR, NLP, and deep learning. It also includes a secure user authentication system built with Node.js and MongoDB. It is designed to classify scanned financial documents into categories such as:

- Balance Sheets
- Cash Flow Statements
- Income Statements
- Notes
- Others

---

## Features

- **OCR Processing**: Extract text from images of financial documents (e.g., `.jpg`, `.jpeg`, `.png`).
- **Data Cleaning**: Preprocess extracted text to remove noise and standardize the format.
- **Classification**: Classify financial documents into categories using a trained machine learning model.
- **Web Interface**: Upload documents via a user-friendly dashboard.
- **Secure**: Bank-level security for user data.

---

## 🗂️ Project Structure

```
MoneyMatic/
├── backend/
│   ├── app.py
│   ├── utils/
│   │   ├── extract_and_prepare.py
│   │   └── other_utils.py
│   ├── model/
│   │   └── financial_text_classifier.joblib
│   └── uploads/
│
├── frontend/
│   ├── index.html
│   ├── login/
│   │   ├── dashboard.html
│   │   └── signup.html
│   ├── CSS/
│   │   └── styles.css
│   └── img/
│
├── moneymatic-backend/
│   ├── server.js
│   ├── config/
│   │   └── db.js
│   ├── routes/
│   │   └── auth.js
│   └── middleware/
│       └── auth.js
│
└── README.md

```

## ⚙️ Installation

### Prerequisites

1. **Python**: Version 3.8 or higher.
2. **Node.js**: Version 14 or higher.
3. **Tesseract OCR**: Install from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract).
4. **MongoDB**: For user authentication and data storage.

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mushxoxo/MoneyMatic.git
   cd MoneyMatic
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv1
   source venv1/bin/activate  # On Windows: venv1\Scripts\activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tesseract OCR:**

   - **Ubuntu:**

     ```bash
     sudo apt update
     sudo apt install tesseract-ocr
     ```

   - **macOS (using Homebrew):**

     ```bash
     brew install tesseract
     ```

   - **Windows:**

     Download and install from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract).

---

## ▶️ Running the Application

1. **Navigate to the backend directory:**

   ```bash
   cd backend
   ```

2. **Start the Flask application:**

   ```bash
   python app.py
   ```
3. **Navigate to the moneymatic-backend directory:**

   ```bash
   cd moneymatic-backend
   ```

4. **Start the Node.js server:**

   ```bash
   node server.js
   ```

5. **Access the web interface:**

   Open your browser and go to [http://localhost:5000](http://localhost:5000)

6. **Login or sign-up using an email id**

7. **Upload and classify documents:**

   - Click on the upload button to select a `.jpg` or `.png` file.
   - View the predicted category, confidence score, and extracted text.

---

## 📈 Model Training (Optional)

If you wish to retrain the model:

1. **Prepare your dataset:**

   - Organize images into subdirectories named after their respective categories.

2. **Run all the scripts in the utils directory:**

   Ensure that the script paths and parameters are correctly set according to your dataset.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👥 Contributors

- [Jyot Shah](https://github.com/Jyot-Shah)
- [Tanmaya Raghuwanshi](https://github.com/Tanmaya113)
- [Arnav Verma](https://github.com/1M-ARNAVERMA)
- [Bhanu Agrawal](https://github.com/mushxoxo)

---
