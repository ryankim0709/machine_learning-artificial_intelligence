# Importing
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