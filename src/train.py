import pandas as pd
import pickle
import argparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def train(data_file, model_file):
    df = pd.read_csv(data_file)
    X = df["review"]
    y = df["label"]

    vectorizer = CountVectorizer(max_features=5000)
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_vec, y)

    with open(model_file, "wb") as f:
        pickle.dump((vectorizer, model), f)

    print(f"✅ Model trained and saved to {model_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--model", required=True)
    args = parser.parse_args()
    train(args.data, args.model)
