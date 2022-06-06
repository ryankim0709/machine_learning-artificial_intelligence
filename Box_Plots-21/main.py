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

lst = [3,9,6,10,7,8,7,6,1]
lst = pd.Series(lst)
print(lst.describe()) # Print info such as mean, median ..
plt.figure(figsize=(20,2))
sns.boxplot(lst)