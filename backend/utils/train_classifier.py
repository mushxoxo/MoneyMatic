import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("utils/cleaned_financial_text_data.csv")

df.dropna(subset=['clean_text', 'label'], inplace=True)

X_train, X_test, y_train, y_test = train_test_split(
    df['clean_text'], df['label'], test_size=0.2, random_state=42, stratify=df['label'])

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=1000, ngram_range=(1, 2))),
    ('clf', LogisticRegression(solver='liblinear', C=1.0))
])

pipeline.fit(X_train, y_train)
print("✅ Model trained!")

y_pred = pipeline.predict(X_test)
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

joblib.dump(pipeline, "model/financial_text_classifier.joblib")
print("\n💾 Model saved to financial_text_classifier.joblib")
