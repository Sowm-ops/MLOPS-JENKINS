import os
import pandas as pd
import pickle
import argparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Processed CSV input")
    parser.add_argument("--model", required=True, help="Path to save model")
    args = parser.parse_args()

    df = pd.read_csv(args.data)
    X = df["review"]
    y = df["label"]

    vectorizer = CountVectorizer(max_features=5000)
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_vec, y)

    # ✅ Create folder before saving
    os.makedirs(os.path.dirname(args.model), exist_ok=True)

    with open(args.model, "wb") as f:
        pickle.dump((vectorizer, model), f)

    print(f"✅ Model trained and saved to {args.model}")
