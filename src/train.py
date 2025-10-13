import yaml
import json
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import pandas as pd

# --- Load Params ---
with open('params.yaml') as f:
    params = yaml.safe_load(f)

learning_rate = float(params.get('learning_rate', 0.001))
epochs = int(params.get('epochs', 5))
batch_size = int(params.get('batch_size', 32))

print(f"Training with learning_rate={learning_rate}, epochs={epochs}, batch_size={batch_size}")

# --- Load Preprocessed Data ---
train_df = pd.read_csv('data/processed/train.csv')
test_df = pd.read_csv('data/processed/test.csv')

X_train, y_train = train_df['text'], train_df['label']
X_test, y_test = test_df['text'], test_df['label']

# --- Feature Extraction ---
vectorizer = TfidfVectorizer(max_features=10000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# --- Train Model (simple logistic regression) ---
model = LogisticRegression(max_iter=epochs, solver='lbfgs')
model.fit(X_train_vec, y_train)

# --- Evaluate ---
y_pred = model.predict(X_test_vec)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.4f}")

# --- Save Artifacts ---
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

metrics = {"accuracy": acc, "epochs": epochs, "learning_rate": learning_rate}
with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)
