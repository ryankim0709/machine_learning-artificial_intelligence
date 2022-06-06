import pandas as pd
from sklearn.ensemble import RandomForestClassifier

exo_train_df = pd.read_csv('https://s3-student-datasets-bucket.-.online/--ds-datasets/kepler-exoplanets-dataset/exoTrain.csv')
exo_test_df = pd.read_csv('https://s3-student-datasets-bucket.-.online/--ds-datasets/kepler-exoplanets-dataset/exoTest.csv')
print(exo_train_df.shape) # => (5087, 3198)
print(exo_test_df.shape) # => (570, 3198)

print(exo_test_df["LABEL"].value_counts()) # Counts the amount of distint values in the "LABEL" column

x_train = exo_train_df.iloc[:,1:] 
y_train = exo_train_df.iloc[:, 0]
print("X training data",x_train)
print("Y training data", y_train)

rf_clf = RandomForestClassifier(n_jobs=-1, n_estimators=50)
rf_clf.fit(x_train, y_train) # Fitting the model
print(rf_clf.score(x_train, y_train)) # Seeing how accurate this model is for the training data set

# Now we must make predictions using this trained model
x_test = exo_test_df.iloc[:,1:]
y_test = exo_test_df.iloc[:,0]

prediction = rf_clf.predict(x_test) # Predicting what we would get for x_test data set from our trained tree
print(prediction)
print(type(prediction)) # => numpy.ndarray

prediction = pd.Series(prediction) # If we convert to pandas series
print(prediction.value_counts()) # We can see our prediction results