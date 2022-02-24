import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft

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

norm_train_df.insert(loc=0, column="LABEL", value=exo_train_df["LABEL"])
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

# Applying the transformation
star_0 = norm_train_df.iloc[0, 1:]
fft_star_0 = np.abs(np.fft.fft(star_0))
print(star_0.head())

freq = np.fft.fftfreq(len(star_0))

plt.figure(figsize=(10, 8))
plt.plot(freq, fft_star_0)
plt.show()
# There are too many values here, so we can zoom in on the first 10 values

plt.figure(figsize=(10,8))
plt.plot(freq[:10], fft_star_0[:10])
plt.show()
# We can now observe the spike within the first 10 values

# Applying Fast Fourier Transformation on dataframes
def fast_fourier_transformation(star):
    return np.abs(np.fft.fft(star, n=len(star))) # N is how long the output should be

x_fft_train = norm_train_df.iloc[:,1:].T.apply(fast_fourier_transformation, axis=0).T
print(x_fft_train.head())
# First 5 values of the transformed data

for i in range(34, 36):
    plt.figure(figsize=(4,4))
    plt.xlabel(str(i))
    plt.ylabel("Flux")
    plt.plot(freq, x_fft_train.iloc[1,:])
    plt.show()


norm_test_df = exo_test_df.iloc[:,1:].apply(mean_normalize, axis=1)
norm_test_df.insert(loc=0, column="LABEL", value=exo_train_df["LABEL"])
norm_test_df.T
star_test = np.abs(np.fft.fft(norm_train_df.iloc[0, 1:]))

x_fft_test = norm_test_df.iloc[:,1:].T.apply(fast_fourier_transformation, axis=0).T
freq = np.fft.fftfreq(len(star_test))

for i in range(3, 8):
    plt.figure(figsize=(8,8))
    plt.xlabel(str(i))
    plt.ylabel("FLUX")
    plt.plot(freq, x_fft_test.iloc[i,:])
    plt.show()