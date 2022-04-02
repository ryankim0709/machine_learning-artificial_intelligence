import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

exo_train_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTrain.csv')
exo_test_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTest.csv')

print(exo_train_df.shape)

def mean_normalise(series): # Data normalisation
    # (Current - mean)/(max - min)
    norm_series = (series - series.mean()) / (series.max() - series.min())
    return norm_series

norm_train_df = exo_train_df.iloc[:,1:].apply(mean_normalise, axis=1)
# For every row, apply for every row
norm_train_df.insert(loc=0, column="LABEL", value=exo_train_df["LABEL"])

norm_test_df = exo_test_df.iloc[:,1:].apply(mean_normalise, axis=1)
norm_test_df.insert(loc=0, column="LABEL", value=exo_test_df["LABEL"])

exo_test_df.T # Transpose (Flip row and columns)

def fast_fourier_transform(star):
  fft_star = np.fft.fft(star, n=len(star))
  return np.abs(fft_star)

print(np.fft.fftfreq(len(exo_train_df.iloc[0, 1:])))

# Apply transformation
x_fft_train_T = norm_train_df.iloc[:,1:].T.apply(fast_fourier_transform)
x_fft_test_T = norm_test_df.iloc[1,:].apply(fast_fourier_transform)

x_fft_train = x_fft_train_T.T
x_fft_test = x_fft_test_T.T

# Preparing for data synthesis
y_train = norm_train_df["LABEL"]
y_test = norm_test_df["LABEL"]

# Data synthesis 
smote = SMOTE(sampling_strategy=1)

x_fft_train_res, y_fft_train_res = smote.fit_resample(x_fft_train_T, y_train)

print(x_fft_train_res.value_counts())
# As you can see, the number of LABEL 1's and 2's are the same!

rf_clf = RandomForestClassifier(n_jobs=-1, n_estimators=50)
rf_clf.fit(x_fft_train_res, y_fft_train_res)
y_pred = rf_clf.predict(x_fft_test)
print(y_pred)

cm = confusion_matrix(y_test, y_pred)
print(classification_report(y_test, y_pred))

# As you can see, even after all of the normalisation, oversampling, and Random Forest Classifier, the model is not the accurate.
# We will now try the XGBoost model (in a different file)