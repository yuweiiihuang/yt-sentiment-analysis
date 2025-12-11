# YouTube Comments Sentiment Analysis

TODO

## Results

TODO

### naive-bayes

```
Accuracy: 0.7030

Classification Report:
               precision    recall  f1-score   support

           0     0.4081    0.6895    0.5127       467
           1     0.6277    0.4411    0.5181       925
           2     0.8290    0.8119    0.8204      2281

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
Test accuracy: 0.6422542880479173

Test Set Classification Report:
              precision    recall  f1-score   support

    negative       0.31      0.81      0.45       467
     neutral       0.54      0.45      0.49       925
    positive       0.93      0.69      0.79      2281

    accuracy                           0.64      3673
   macro avg       0.59      0.65      0.58      3673
weighted avg       0.76      0.64      0.67      3673

One-vs-Rest AUC:
AUC for negative (0): 0.8589
AUC for neutral (1): 0.8131
AUC for positive (2): 0.8885

Confusion Matrix (rows = true, cols = predicted):
[[ 380   48   39]
 [ 438  415   72]
 [ 414  303 1564]]
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