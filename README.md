# YouTube Comments Sentiment Analysis

TODO

## Results

TODO

### naive-bayes

```
Accuracy: 0.7030

Classification Report:
               precision    recall  f1-score   support

    negative     0.4081    0.6895    0.5127       467
     neutral     0.6277    0.4411    0.5181       925
    positive     0.8290    0.8119    0.8204      2281

    accuracy                         0.7030      3673
   macro avg     0.6216    0.6475    0.6171      3673
weighted avg     0.7248    0.7030    0.7051      3673


One-vs-Rest AUC:
AUC for Negative (0): 0.8623
AUC for Neutral (1): 0.8152
AUC for Positive (2): 0.8631

Confusion Matrix (rows = true, cols = predicted):
[[ 322   48   97]
 [ 232  408  285]
 [ 235  194 1852]]
```

### lstm

```
Accuracy: 0.7493

Classification Report:
              precision    recall  f1-score   support

    negative     0.4967    0.6403    0.5594       467
     neutral     0.5822    0.6854    0.6296       925
    positive     0.9178    0.7975    0.8534      2281

    accuracy                         0.7493      3673
   macro avg     0.6655    0.7077    0.6808      3673
weighted avg     0.7797    0.7493    0.7597      3673


One-vs-Rest AUC:
AUC for negative (0): 0.8918
AUC for neutral (1): 0.8630
AUC for positive (2): 0.9134

Confusion Matrix (rows = true, cols = predicted):
[[ 299  115   53]
 [ 181  634  110]
 [ 122  340 1819]]
```

### bert-fine-tuning

```
Test Accuracy: 0.82

Test Set Classification Report:
              precision    recall  f1-score   support

    Negative       0.70      0.68      0.69       467
     Neutral       0.69      0.70      0.69       925
    Positive       0.90      0.90      0.90      2281

    accuracy                           0.82      3673
   macro avg       0.76      0.76      0.76      3673
weighted avg       0.82      0.82      0.82      3673
```

## References

- Dataset\
[atifaliak/youtube-comments-dataset](https://www.kaggle.com/datasets/atifaliak/youtube-comments-dataset)

- Naive Bayes\
[atifaliak/sentiment-analysis-on-youtube-comments](https://www.kaggle.com/code/atifaliak/sentiment-analysis-on-youtube-comments)

- LSTM\
[muhammedaliyilmazz/lstm-based-sentiment-analysis-for-youtube-data](https://www.kaggle.com/code/muhammedaliyilmazz/lstm-based-sentiment-analysis-for-youtube-data)

- BERT-fine-tuning\
[chriskhanhtran/bert-for-sentiment-analysis](https://github.com/chriskhanhtran/bert-for-sentiment-analysis?tab=readme-ov-file)