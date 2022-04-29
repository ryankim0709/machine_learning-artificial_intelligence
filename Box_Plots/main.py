import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

met_df = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/meteorite-landings/meteorite-landings.csv")
print(met_df.head())
print(met_df.shape()) # (rows, columns)
print(met_df["year"].describe()) # count, mean, std(std dev), min, etc

plt.figure(figsize=(20,2))
sns.boxplot(met_df["year"])

plt.figure(figsize=(20,2))
sns.boxplot(met_df["mass"])

