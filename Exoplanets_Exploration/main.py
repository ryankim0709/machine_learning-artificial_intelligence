import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading from CSV file
exo_train_df = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTrain.csv")
# This will create a table of the data

print(exo_train_df.shape) # => (570, 3198)
print(exo_train_df.isnull().sum()) # => sum of the number of null values
print(exo_train_df.columns) # => columns in the data
print(exo_train_df["FLUX.1"]) # => Data for Flux 1 for each star
print(exo_train_df.head()) # First 5 values
print(exo_train_df.tail()) # Last 5 values

# Finding the number of missing values
missing_vals = 0

for i in exo_train_df.columns:
    for j in exo_train_df[i].isnull():
        if j == False:
            missing_vals += 1

print(missing_vals) # 0 missing values!

# Getting star 0
star_0 = exo_train_df.iloc[0,:] # Getting the first star, then all of its data

# Data visualization
# If the data has periodic dips, it shows that there is a star around that planet

x_values_star_0 = np.arange(1, 3198)
y_values_star_0 = star_0[1:]

plt.figure(figsize=(16,4)) # => You can resize the pyplot using this
plt.scatter(x_values_star_0, y_values_star_0) # Scatter plot
plt.show() # The graph shows periodic dips which means that there is a planet orbiting it!

plt.figure(figsize=(16,4))
plt.plot(x_values_star_0, y_values_star_0) # Line plot
plt.show() # The graph shows periodic dips which means that there is a planet orbiting it!