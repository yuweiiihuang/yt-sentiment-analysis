from pathlib import Path
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split


RAW_DATA_PATH = Path("dataset/raw/YoutubeCommentsDataSet.csv")
OUTPUT_DIR = Path("dataset/processed")
TRAIN_OUTPUT = OUTPUT_DIR / "train.csv"
TEST_OUTPUT = OUTPUT_DIR / "test.csv"


def split_dataset(test_size: float) -> None:
    df = pd.read_csv(RAW_DATA_PATH)

    # Drop rows missing either comment text or label to keep splits clean.
    df = df.dropna(subset=["Comment", "Sentiment"])

    if df.empty:
        raise ValueError("No data available after dropping missing rows.")

    train_df, test_df = train_test_split(
        df,
        test_size=test_size,
        random_state=42,
        stratify=df["Sentiment"],
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    train_df.to_csv(TRAIN_OUTPUT, index=False)
    test_df.to_csv(TEST_OUTPUT, index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Split YoutubeCommentsDataSet.csv into stratified train/test CSVs."
    )
    parser.add_argument(
        "--test-size",
        type=float,
        default=0.2,
        help="Proportion of the dataset to include in the test split (default: 0.2).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    split_dataset(test_size=args.test_size)
