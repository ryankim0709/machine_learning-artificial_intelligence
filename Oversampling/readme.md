## Oversampling - SMOTE - 20

Oversampling is forcefully adding more data into the dataset so that the number of occurences of each target variable is the same.
In a nutshell, oversampling is synthesizing data in order to create a more even dataset.

There are 3 main ways to synthesize data
    - Random Oversampling
    - SMOTE
    - ADASYN

To apply smote
    - ```from imblearn.over_sampling import SMOTE```
    - Call the ```SMOTE()``` function with ```sampling_strategy=1```
        - This means that after resampling, the number of datapoints for both the majority and minority class should be the same
    - Apply ```fit_resample()``` from ```SMOTE``` module to syntehsize data for minority class