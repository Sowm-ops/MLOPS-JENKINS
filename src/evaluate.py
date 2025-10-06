import pandas as pd
import pickle
import argparse
from sklearn.metrics import accuracy_score
import json

def evaluate(data_file, model_file, metrics_file):
    df = pd.read_csv(data_file)
    X = df["review"]
    y = df["label"]

    with open(model_file, "rb") as f:
        vectorizer, model = pickle.load(f)

    X_vec = vectorizer.transform(X)
    preds = model.predict(X_vec)
    acc = accuracy_score(y, preds)

    metrics = {"accuracy": round(acc, 4)}
    with open(metrics_file, "w") as f:
        json.dump(metrics, f)

    print(f"Evaluation complete. Accuracy: {acc:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--metrics", required=True)
    args = parser.parse_args()
    evaluate(args.data, args.model, args.metrics)
