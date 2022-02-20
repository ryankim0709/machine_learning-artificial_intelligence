## Confusion Matrix

A confusion matrix is how a classification model is **generally evaluated**
A confusion is essentially a 2 X 2 array

In a confusion matrix, we look at the expected outcmoe and the predicted outcome.

|              | Predicted | Negative       | Positive       |
| ------------ | --------- | -------------- | -------------- |
| **Actual**   |           |                |                |
| **Negative** |           | True Negative  | False Positive |
| **Positive** |           | False Negative | True Positive  |

Essentially these values in the table is `Predicted == Actual` `Predicted_Value`.
We now know that `correctly_classified = true_positive + true_negative` and that `incorrectly_classified = false_positive + false_negative`.

**Precision - Accuracy of our model**

<img src="https://latex.codecogs.com/svg.image?\inline&space;Precision&space;=&space;\frac{True&space;Positive}{True&space;Positive&space;&plus;&space;False&space;Positive}" title="\inline Precision = \frac{True Positive}{True Positive + False Positive}" />

**Recall - How many True Positives were found**

<img src="https://latex.codecogs.com/svg.image?\inline&space;Recall&space;=&space;\frac{True&space;Positive}{True&space;Positive&space;&plus;&space;False&space;Negative}" title="\inline Recall = \frac{True Positive}{True Positive + False Negative}" />

**F1 Score - Cumulative accuracy**

<img src="https://latex.codecogs.com/svg.image?\inline&space;f1-score&space;=&space;2\frac{precision&space;*&space;recal}{precision&space;&plus;&space;recall}&space;=&space;\frac{True&space;Positive}{True&space;Positive&space;&plus;&space;\frac{1}{2}(False&space;Positive&space;&plus;&space;False&space;negative)}" title="\inline f1-score = 2\frac{precision * recal}{precision + recall} = \frac{True Positive}{True Positive + \frac{1}{2}(False Positive + False negative)}" />

\*\*F1 Score - Cumulative accuracy

Many people often mix up precision and F1 Score. In precision you are comparing the number of True Positives against False Positive, but in F1 Score
you compare True Positive against the sum of False Positive **and** False Negative which incapsulates all of our data.
