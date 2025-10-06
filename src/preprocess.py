import os
import pandas as pd

def load_imdb_dataset(data_dir):
    rows = []
    for label in ["pos", "neg"]:
        folder = os.path.join(data_dir, label)
        for fname in os.listdir(folder):
            if fname.endswith(".txt"):
                with open(os.path.join(folder, fname), "r", encoding="utf-8") as f:
                    text = f.read().strip()
                rows.append({"review": text, "label": 1 if label == "pos" else 0})
    return pd.DataFrame(rows)

if __name__ == "__main__":
    raw_dir = "data/raw/aclImdb/train"
    df = load_imdb_dataset(raw_dir)
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/imdb_clean.csv", index=False)
    print(" Preprocessed IMDb dataset saved.")
