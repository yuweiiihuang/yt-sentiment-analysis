# YouTube Comments Sentiment Analysis

## Environment Setup

- Python 3.11 recommended.
- Create and activate a virtual environment:
  - `python -m venv .venv`
  - `source .venv/bin/activate` or `.venv\Scripts\activate` (Windows)
- Install dependencies: `pip install -r requirements.txt`

## Prepare Dataset

1. Raw CSV expected at `dataset/raw/YoutubeCommentsDataSet.csv`.
2. Split into train/test: `python split_dataset.py`
  - Outputs go to `dataset/processed/train.csv` and `dataset/processed/test.csv`.

## How to Run

- Start Jupyter: `jupyter notebook`
- Notebooks to execute:
  - `naive-bayes.ipynb`: TF-IDF + Naive Bayes with randomized search; saves predictions to `outputs/naive-bayes/`.
  - `lstm.ipynb`: LSTM with pretrained GloVe Twitter embeddings from `dataset/embeddings/`; saves to `outputs/lstm/`.
  - `bert-fine-tuning.ipynb`: Fine-tunes multilingual BERT; GPU recommended; saves to `outputs/bert/`.

## How to Reproduce

1. Run the three model notebooks (Run All). Each notebook sets seeds and writes test predictions/metrics under its `outputs/<model>/` folder.
2. Open `aggregate_outputs.ipynb` and Run All to recompute the metrics table and plots from the generated outputs.

## Results

| Model               |     Accuracy    |    Macro F1     |    Macro AUC    |
|---------------------|-----------------|-----------------|-----------------|
| Naive Bayes         | 0.7030 ± 0.0023 | 0.6182 ± 0.0033 | 0.8522 ± 0.0037 |
| LSTM                | 0.7531 ± 0.0049 | 0.6885 ± 0.0051 | 0.8937 ± 0.0025 |
| BERT Fine-Tuning    | 0.8134 ± 0.0029 | 0.7598 ± 0.0038 | 0.9342 ± 0.0009 |

More charts and analysis can be found in the [notebook](aggregate_outputs.ipynb).

## References

- Dataset: [atifaliak/youtube-comments-dataset](https://www.kaggle.com/datasets/atifaliak/youtube-comments-dataset)

- Naive Bayes: [atifaliak/sentiment-analysis-on-youtube-comments](https://www.kaggle.com/code/atifaliak/sentiment-analysis-on-youtube-comments)

- LSTM: [muhammedaliyilmazz/lstm-based-sentiment-analysis-for-youtube-data](https://www.kaggle.com/code/muhammedaliyilmazz/lstm-based-sentiment-analysis-for-youtube-data)

- BERT-fine-tuning: [chriskhanhtran/bert-for-sentiment-analysis](https://github.com/chriskhanhtran/bert-for-sentiment-analysis?tab=readme-ov-file)
