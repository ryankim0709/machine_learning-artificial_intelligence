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
