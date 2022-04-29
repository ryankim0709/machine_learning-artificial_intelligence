import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
import xgboost as xg
from sklearn.metrics import confusion_matrix, classification_report

exo_train_df = pd.read_csv('https://s3-student-datasets-bucket.-.online/--ds-datasets/kepler-exoplanets-dataset/exoTrain.csv')
exo_test_df = pd.read_csv('https://s3-student-datasets-bucket.-.online/--ds-datasets/kepler-exoplanets-dataset/exoTest.csv')

def mean_normalize(series):
  # Normalization
  norm_series = (series - series.mean()) / (series.max() - series.min())
  return norm_series

def fast_fourier_transform(star):
  # Apply Fast Fourier
  fft_star = np.fft.fft(star, n=len(star))
  return np.abs(fft_star)

norm_train_df = exo_train_df.iloc[:, 1:].apply(mean_normalize, axis=1)
norm_train_df.insert(loc=0, column="LABEL", value=exo_train_df["LABEL"])
# Apply normalization and insert label

norm_test_df = exo_test_df.iloc[:,1:].apply(mean_normalize, axis=1)
norm_test_df.insert(loc=0, column="LABEL", value=exo_test_df["LABEL"])
# Apply normalization and insert label

x_fft_train_T = norm_train_df.iloc[:,1:].T.apply(fast_fourier_transform)
x_fft_train = x_fft_train_T.T
# Apply fast fourier and transpose
x_fft_test_T = norm_test_df.iloc[:,1:].T.apply(fast_fourier_transform)
x_fft_test = x_fft_test_T.T
# Apply fast fourier and transpose

y_train = norm_train_df["LABEL"]
# Y train
y_test = norm_test_df["LABEL"]
# Y test

smote = SMOTE(sampling_strategy=1) # Set up oversampling
x_fft_train_res, y_fft_train_res = smote.fit_resample(x_fft_train, y_train) # Resample given x train and y train

model = xg.XGBClassifier() # XGBoost model
model.fit(x_fft_train_res, y_fft_train_res) # Train model (Takes time)
y_pred = model.predict(x_fft_test) # Prediction
print(y_pred)

cm = confusion_matrix(y_test, y_pred) # Confusion matrix
print(cm)

print(classification_report(y_test, y_pred))
# Success! As you can see, the precision is much higher than the RandomForestClassifier
