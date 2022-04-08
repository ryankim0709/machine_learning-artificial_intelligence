from matplotlib.pyplot import axis
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
import xgboost as xg

exo_train_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTrain.csv')
exo_test_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTest.csv')

def mean_normalise(series):
  norm_series = (series - series.mean()) / (series.max() - series.min())
  return norm_series

def fast_fourier_transform(star):
  fft_star = np.fft.fft(star, n=len(star))
  return np.abs(fft_star)

norm_train_df = exo_train_df.iloc[:, 1:].apply(mean_normalise, axis=1)
norm_train_df.insert(loc=0, column="LABEL", value=exo_train_df["LABEL"])

norm_test_df = exo_test_df.iloc[:,1:].apply(mean_normalise, axis=1)
norm_test_df.insert(loc=0, column="LABEL", value=exo_test_df["LABEL"])

x_fft_train_T = norm_train_df.iloc[:,1:].T.apply(fast_fourier_transform)
x_fft_train = x_fft_train_T.T
x_fft_test_T = norm_test_df.iloc[:,1:].T.apply(fast_fourier_transform)
x_fft_test = x_fft_test_T.T

y_train = norm_train_df["LABEL"]
y_test = norm_test_df["LABEL"]

smote = SMOTE(sampling_strategy=1)
x_fft_train_res, y_fft_train_res = smote.fit_resample(x_fft_train, y_train)

model = xg.XGBClassifier()
model.fit(x_fft_train_res, y_fft_train_res)
y_pred = model.predict(x_fft_test)