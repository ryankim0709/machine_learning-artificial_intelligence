# Create Python list
lst = [1, 2, 3, 4]

# You can mix and match data types
lst = ["Ryan",14,"Palo Alto High", True, 4.0] # Lists can have a variety of data types stored inside

# Indexing
# List indexing in Python starts with 0
lst[0] # => "Ryan"
lst[1] # => 14
lst[2] # => "Palo Alto High"
lst[3] # => True
lst[4] # => 4.0

# Count function .count()
# Count the number 
print(lst.count(1)) # -> 2

# Length of array
print(len(lst))

# Empty list
lst = []

# Append/Adding to an empty list
# Append adds to the end of a list
lst.append(1) # [] -> [1]
lst.append(2) # [1] -> [1, 2]
lst.append(3) # [1, 2] -> [1, 2, 3]
lst.append(4) # [1, 2, 3] -> [1, 2, 3, 4]
lst.append(4) # [1, 2, 3, 4] -> [1, 2, 3, 4, 4]

# Removing items from list

lst.remove(4) # [1, 2, 3, 4, 4] => [1, 2, 3, 4]
# Removes first occurence of 4

lst.append(4) # [1, 2, 3, 4] => [1, 2, 3, 4, 4]
lst.pop() # Removes from end [1, 2, 3, 4, 4] => [1, 2, 3, 4]

lst.append(4) # [1, 2, 3, 4] => [1, 2, 3, 4, 4]
lst.pop(3) # Removes from a giving index [1, 2, 3, 4, 4] => [1, 2, 3, 4]

# Negative Indexing
positive_indexing = [0,1,2,3,4,5] # Usually we start from index zero ...
# When using negative indexing .....
negative_indexing = [-6,-5,-4,-3,-2,-1] # We start from -1
# We don't start from 0 because there is no -0

# Replacing 

# List slicing
# List slicing refers to a shorthand method to get a group of elements in a list

# lst[start:end]
print(lst[0:3]) # Get items in list from [0,3) => Index 0 to 2

# lst[:end]
print(lst[:3]) # Get items from start [0,3) => Index 0 to 2

# lst[:]
print(lst[:]) # Get all of the items

# lst[start:end:step]
print(lst[0:4:2]) # Get items from index 0 to 3 using intervals of 2 => lst[0], lst[2]

# lst[::-steps]
print(lst[::-1]) # Get whole array in reverse order in steps of steps
print(lst[::-2]) # Get whole array in reverse order in steps of steps

# Getting index of item
print(lst.index(2)) # Get the index of an item returns -1 if it is not found

# Replacing items
lst[lst.index(2)] = 1 # Removes index of 0 to one [1, 2, 3, 4] => [1, 1, 3, 4]

# List comprehension
# Quckily building lists
lst = [i for i in range(1, 11)] # List containing numbers from 1 to 10

# Copying contents from old list
lst = [index for index in negative_indexing] # Get data from list above, 'negative indexing'

# Operations
lst = [i + 2 for i in lst] # Add add elements in array by 2
lst = [i - 2 for i in lst] # Subtract add elements in array by 2
lst = [i * 2 for i in lst] # Multiply add elements in array by 2
lst = [i / 2 for i in lst] # Divide add elements in array by 2
lst = [i ** 2 for i in lst] # Square every element in array

# Conditionals in list comprehension
lst = [i for i in range(5) if i % 2 == 0] # => [0, 2, 4] every number from 0 to 4 if it is divisible by 2

# Two dimensional arrays
# Initialization
students = [ # Empty
    []
]
students = [ # With data
    ["Ryan",4.0],
    ["Tony", 4.0],
    ["Kang Hee", 4.0]
]

# Think of a 2-D array as a table

# Indexing
# Row and column both start 0 and we go [row][column]
print(students[1][1]) # Returns 4.0. Looks at 2nd array and the 2nd element of that array
print(students[2]) # Returns ["Kang Hee", 4.0]. Gives the entire 3rd row

# Length of 2-D arrays
print(len(students)) # Returns the number of arrays/rows there are

# List comprehension
ones = [ 
    [1 for i in range(2)]
    for x in range(3)
] 
# 2-D array with subarray, [0, 1] duplicated 3 times

# 3-Dimensional arrays
# Initialization
scores = [ # Empty
    [
        []
    ]
]

scores = [
    [
        [100, 100, 100],
        [90, 100, 80]
    ],
    [
        [100, 100, 100],
        [70, 100, 100]
    ]
]

# Think of 3-D arrays as a cube.
# This array has 2 blocks, with 2 rows and 3 columns each

# Indexing
# Block, Row, and Column start form zero and indexing is in that order
print(scores[1][0][1])
# 2nd block, 1st row, 2nd element

# Length of 3-D array
print(len(scores)) # returns the number of blocks there are

# List comprehension
ones = [
    [
        [1 for i in range(2)]
    ] for x in range(3)
    for z in range(2)
] 

# 3-D array with 2 blocks each with 3 rows and 2 columns all filled with 1's