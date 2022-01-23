# The While loop
# Continuously does something until a condition is met

# Increment values
value = 0
while value < 11: # Numbers from 0 to 10
    print(value)
    value += 1 # Shorthand for adding a number to a number

# Infinite while loops
# while True:
#     print("Continuing")

# For loop

# Increment values
for x in range(0, 11): # For loops are from [num1, num2)
    # Print 0 to 10
    print(x)

# For each loop
lst = ["Ryan",14,"Palo Alto High", True, 4.0]
for info in lst:
    # Print the elements in a list without indexing
    print(info)