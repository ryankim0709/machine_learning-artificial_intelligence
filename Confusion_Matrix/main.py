import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

exo_train_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTrain.csv')
exo_test_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTest.csv')

print(exo_train_df.shape) # => (5087, 3198)
print(exo_test_df['LABEL'].value_counts()) # Counts the distinct labels

x_train = exo_train_df.iloc[:,1:] # x values for training data
print(x_train.head())

y_train = exo_train_df.iloc[:,0] # y values for training data
print(y_train.head())

rf_clf = RandomForestClassifier(n_jobs=-1, n_estimators=50)
rf_clf.fit(x_train, y_train)
print(rf_clf.score(x_train, y_train)) # Accuracy if we use training data sets

x_test = exo_test_df.iloc[:,1:] # x values for testing data
print(x_test.head())
y_test = exo_test_df.iloc[:,0] # y values for testing data
print(y_test.head())

prediction = rf_clf.predict(x_test) # Predict values for x testing data
print(prediction)

prediction = pd.Series(prediction) # To pandas series
print(prediction.head()) # First 5
print(prediction.value_counts()) # See how many of each there are

matrix = confusion_matrix(y_test, prediction)
print(matrix)