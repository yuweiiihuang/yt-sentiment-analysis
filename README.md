# YouTube Comments Sentiment Analysis

TODO

## Results

TODO

### naive-bayes

```
Accuracy: 0.6817

Classification Report:
              precision    recall  f1-score   support

           0     0.3478    0.7216    0.4694       467
           1     0.6308    0.3676    0.4645       925
           2     0.8439    0.8010    0.8219      2281

    accuracy                         0.6817      3673
   macro avg     0.6075    0.6301    0.5852      3673
weighted avg     0.7271    0.6817    0.6870      3673

One-vs-Rest AUC:
AUC for Negative (0): 0.8613
AUC for Neutral (1): 0.8168
AUC for Positive (2): 0.8695

Confusion Matrix (rows = true, cols = predicted):
[[ 337   37   93]
 [ 340  340  245]
 [ 292  162 1827]]
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