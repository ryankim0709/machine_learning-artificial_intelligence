# 13, 14, & 15

from matplotlib.pyplot import axis
import pandas as pd
import random

# A pandas series is a one-dimensional array which hold various data types

# Creating a simple pandas series
weights = pd.Series([random.randint(45,60) for i in range(30)])

# Type of the series
type(weights) # => pandas.core.series.Series

# Size of the series
weights.size # => 30

# Shape of the series
weights.shape # => (30,) 
# Generally in (rows, columns) form

# Simple operations
weights.mean() # => mean of elements
weights.min() # => min of elements
weights.max() # => max of elements
weights.mode() # => mode of elements
weights.median() # => median of elements
weights.head() # => first 5 entries head(n) will return first n
weights.tail() # => last 5 entries tail(n)  will return last n

# Splicing
weights[13:22] # Will slice from index [13,22]

# Sorting
weights = weights.sort_values(ascending=True) # => Sort in ascending order

# Count entry occurences
weights.value_counts() # => counts the number of times an element appears

# Exoplanet Data
exo_train_df = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/--ds-datasets/kepler-exoplanets-dataset/exoTrain.csv")

# Checking if items in series is null
exo_train_df.isnull() # => returns False if there are no null values
exo_train_df.isnull().sum() # => sum of the number of null values

# Columns in a series
exo_train_df.columns # => Gives the columns in a pandas series

# iloc[] function for 2-D pandas series only
# dataframe_name.iloc[row_position_start : row_position_end, column_position_start : column_position_end]

star_0 = exo_train_df.iloc[0,:]
# Getting the first data point, then all of the data in the row

# apply()
# This function allows us to perform a function on every row or column of a pandas series.
# The syntax is datafram.apply(function_name, axis = #)
# If axis = 1, then it means horizantal
# If axis = 0, then it means vertical

def mean_normalise(series):
    # We must be inputed a pandas series
    norm_series = (series - series.mean()/(series.max() - series.min()))
    return norm_series
norm_train_df = exo_train_df.iloc[:,1:].apply(mean_normalise, axis=1)

# insert()
# If we want to add back a column of data to a dataframe, we can call the insert function
# The syntax is dataframe.insert(loc = #, column = "", value=dataframe)

norm_train_df.insert(loc=0, column="LABEL", value=exo_train_df["LABEL"])

# T
# This function is "transpose", it will switch the row and the column for a pandas series
print(norm_train_df.T)