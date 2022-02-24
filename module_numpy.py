# Importing
from pstats import Stats
import numpy as np

# ones() and zeros()
# Create a numpy array filled with ones or zeros
ones = np.ones(shape = (5,3,3), dtype = int) # 3-D array with 5 blocks, 3 rows, 3 columns
zeros = np.zeros(shape = (5,3,3), dtype = int) # 3-D array with 5 blocks, 3 rows, 3 columns
# shape is the configuration of the array in (blocks, rows, columns)

# Dimensions of numpy array
print(ones.ndim) # 3 because it is a 3 dimensional array
print(zeros.ndim) # 3 because it is a 3 dimensional array
print(ones.shape) # (5,3,3) is the shape we specified during initialization
print(zeros.shape) # (5,3,3) is the shape we specified during initialization

# Data type of numpy array
print(ones.dtype) # int64 because it is a 64 bit integer

# arrange()
# Returns a one-dimensional array containing numbers between two specific numbers from [start, end)
arr = np.arange(2, 5) # [2, 3, 4]
arr = np.arange(1, 25, 4, dtype=float) # [1, 5, 9, 13, 17,21]
# From 1 to 24 in intervals of 4 using the float data type

# linspace()
# Returns a one-dimensional arry containing n numbers, equally spaced from start to end [start, end]
arr = np.linspace(1, 25, 4) # [1, 9, 17, 25]
# There are 4 numbers in the array and they are all equally spaced with increasing intervals of 8

# reshape()
# Enables you to reshape the dimensions of an array. Make sure the number of elements are still the same
# Recall that our 'zeros' array had shape (5, 3, 3)
zeros = zeros.reshape(45) # 1-D array of 45
zeros = zeros.reshape(5, 9) # 2-D array of 5 rows and 9 columns

# ndarray()
# Create an array giving shape and data type
arr = np.ndarray((5,2), dtype = int)
# 2-D array with 5 rows and 2 columns, filled with random integers

# np.random.randint()
# Create an array from [start, end) with n elements
arr = np.random.randint(50, 101, size=(10))
arr = np.random.randint(50, 101, size=(2, 5))
arr = np.random.randint(50, 101, size=(2, 5, 1))
# array with random integers from [50, 101) with shape

# array()
# Convert python list into NumPy array
arr = np.array([x for x in range(50)])

# list()
# Convert NumPy list to python list
arr = list(arr)

# sqrt()
np.sqrt(100) # Gives square root value

# Length of NumPy arrays
arr = np.arange(1, 25)
len(arr) # => 24 because there are 24 numbers in the 1-D array
arr = np.arange(1,29).reshape(4,7)
len(arr) # => 4 because there are 4 rows in the 2-D array
arr = np.arange(1,31).reshape(3,2,5)
len(arr) # => 3 because there are 3 blcoks in the 3-D array

# Size of NumPy arrays
arr = np.arange(1, 25)
arr.size() # => 24 because there are 24 elements in the 1-D array
arr = np.arange(1,29).reshape(4,7)
arr.size() # => 28 because there are 28 elements in the 2-D array
arr = np.arange(1,31).reshape(3,2,5)
arr.size() # => 30 because there are 30 elements in the 3-D array

# Statistics using NumPy
phones = np.array([1,1,1,2,2])
stock = np.array([1,1,1,2,2])

# Operations on NumPy arrays
total = phones * stock # => [1,1,1,4,4]
total = phones + stock # => [2,2,2,4,4]
total = phones - stock # => [0,0,0,0,0]
total = phones / stock # => [1,1,1,1,1]
# Each element of the arrays will be multiplied, added, subtracted, or divided

# Statistical values of NumPu arrays
np.sum(total) # Sum of array
np.mean(total) # Mean of array
np.min(total) # Minimum value
np.max(total) # Maximum value
np.median(total) # Median value
# There is no function for mode, but you can do
from scipy import stats
stats.mode(total)

# More operatiosn on NumPy arrays
import random
radii = np.array([random.randint(1, 10) for x in range(20)])
radii = radii ** 2
# Raise every element to the power of 2

# Making all elements positive
print(np.abs(np.arange(-10, 100)) )
# This will change all of the array items to their absolute value

# Applying Fast Fourier Transormation
print(np.fft.fft(np.arange(10, 100)))
# This will apply the Fast Fourier Transformation to our numpy array elements

# Finding the frequencies that we need for our Fast Fourier Graph
print(np.fft.fftfreq(len(np.arange(10, 100))))
# Creates needed frequencies for the fast fourier graph