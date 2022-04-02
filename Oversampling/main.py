import numpy as np
import pandas as pd

exo_train_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTrain.csv')
exo_test_df = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTest.csv')

print(exo_train_df.shape)

def mean_normalise(series): # Data normalisation
    # (Current - mean)/(max - min)
    norm_series = (series - series.mean()) / (series.max() - series.min())
    return norm_series