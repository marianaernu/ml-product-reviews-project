import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

#  1. Încarcăm datele 
df = pd.read_csv("data/products.csv")

#  2. Curățare coloane 
df.columns = [c.strip() for c in df.columns]

# 3. Curățare titluri 
def clean_title(s):
    if pd.isna(s):
        return ""
    s = str(s).lower()
    s = re.sub(r"[^a-z0-9\u00C0-\u017F\s\-\_\.]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

df['clean_title'] = df['Product Title'].apply(clean_title)

#  4. Eliminăm rânduri cu valori lipsă 
df = df.dropna(subset=['Category Label', 'clean_title'])

# 5. Împărțire train/test 
X = df['clean_title']
y = df['Category Label']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

#  6. Vectorizare TF-IDF 
vectorizer = TfidfVectorizer(max_features=30000, ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 7. Antrenare model Logistic Regression 
model = LogisticRegression(max_iter=1000, solver='saga', n_jobs=-1)
model.fit(X_train_vec, y_train)

# 8. Salvare model 
os.makedirs("models", exist_ok=True)
with open("models/product_category_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print(" Model antrenat și salvat în models/product_category_model.pkl")