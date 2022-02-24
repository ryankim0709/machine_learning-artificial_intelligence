import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

exo_train_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTrain.csv')
exo_test_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTest.csv')

print(exo_train_df.shape)
print(exo_test_df.shape)

# Normalization
def mean_normalize(series):
    norm_series = (series - series.mean())/(series.max() - series.min())
    return norm_series

norm_train_df = exo_test_df.iloc[:,1:].apply(mean_normalize, axis=1)
print(norm_train_df.head())

norm_train_df.insert(loc=0, column="LABEL", value=exo_test_df["LABEL"])
print(norm_train_df.head())

# Transposing data
norm_train_df.T

# Plotting data
x_axis = np.arange(3197)
plt.figure(figsize=(10,8))
plt.plot(x_axis, norm_train_df.iloc[0,1:])
plt.show()

frequency = 1/365.25
frequency *= 1/24 * 1/60 * 1/60