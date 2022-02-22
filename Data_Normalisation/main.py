import pandas as pd
import numpy as np

# Normalising function
def mean_normalise(series):
    # We must be inputed a pandas series
    norm_series = (series - series.mean()/(series.max() - series.min()))
    return norm_series

exo_train_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTrain.csv')
exo_test_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTest.csv')

print(exo_train_df.shape) 
print(exo_test_df.shape)

print(exo_train_df.describe()) # Print specifics about our data

# As you can see, the difference between the min and the max is 10^6, which is huge.
# We will use mean normalisation in order to decrease this number

norm_train_df = exo_train_df.iloc[:,1:].apply(mean_normalise, axis=1)
print(norm_train_df.head())
print(norm_train_df.describe())
# As you can see, the difference is much smaller now which means our normalisation has worked!

# We normalised just the flux's, so we must put the labels back
norm_train_df.insert(loc = 0, column="LABEL", value = exo_train_df["LABEL"])
print(norm_train_df.head())

# As you can see, we have added our "LABEL" row back!