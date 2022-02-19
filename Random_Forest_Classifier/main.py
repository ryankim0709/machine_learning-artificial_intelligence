import pandas as pd
from sklearn.ensemble import RandomForestClassifier

exo_train_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTrain.csv')
exo_test_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTest.csv')
print(exo_train_df.shape) # => (5087, 3198)
print(exo_test_df.shape) # => (570, 3198)

print(exo_test_df["LABEL"].value_counts()) # Counts the amount of distint values in the "LABEL" column
