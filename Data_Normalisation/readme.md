## Data Normalisation

Data normalisation is the process of standardizing data. We do this to bring all of
our data to a uniform scale.

Data normalisation is needed because if there is a large variance in the data, then
the AI can develop a **bias** which will yield to incorrect results.

**Why?**

This is because machine learning models are **sensitive** to the **scale of data**.
Models will give more importance to larger values which is how bias is developed.

**Disclaimer! There are many types of data normalisation, but I will be exploring
mean normalisation for the time being**

## Mean Normalisation

To do this, we will follow these simple steps

Given `x_1, x_2, x_3, ..., x_n`

- `x_mean` is the mean of the array
- `x_min` is the minimum of the array
- `x_max` is the maximum of the array
- <img src="https://latex.codecogs.com/svg.image?\inline&space;x_{norm}&space;=&space;\frac{x_{p}&space;-&space;x_{mean}}{x_{max}&space;-&space;x_{min}}" title="\inline x_{norm} = \frac{x_{p} - x_{mean}}{x_{max} - x_{min}}" />

## New things that were used

**apply() function**

Syntax: `dataframe.apply(functionName, axis = #)`

The apply function allows us to apply a function to every row or column of a pandas series

If `axis == 0`, we are applying the function for every column

If `axis == 1`, we are applying the function for every row

**insert() function**

Syntax: `dataframe.insert(loc = #, column = "", value = dataframe)`

The insert function allows to add a column to our dataframe at certain location
with a certain name

`loc` argument is the location of where to insert. Starts with 0

`column` argument is the name of the column

`value` argument is the series that should be inserted
