## Data Transformation - 19

We will be applying **Fast Fourier Transformation** to our dataframe to determine
whether the incease/decrease of light is periodic or not.

**Frequency**

Frequency is the length of one second. Frequency is measured in **Hertz** denoted as
**Hz**. Frequency is defined as <img src="https://latex.codecogs.com/svg.image?\inline&space;f=\frac{1}{Time}" title="\inline f=\frac{1}{Time}" />.

**1 Hz = 1 Second**

**Amplitude** is the peak value of a wave.

## Applying Fast Fourier

1. Transpose Data
   - Flip X and Y axis of dataframe
2. Convert the time dependent data into frequency dependant data.
   - This will help is identify how many periodic signals exist.
3. Transpose Data
   - Flip X and Y axis of dataframe
