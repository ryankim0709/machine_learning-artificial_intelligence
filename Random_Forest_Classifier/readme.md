## Exoplanets Random Forest Classifier

A **Random Forest Classifier** is a collection/ensemble of many decision trees.
<br/>
A decision tree is a **flow chart** which separates data based on sets of conditions.

**About the Random Forest Classifier**
<br/>
**Setting it up**
To set up the Random FOrest Classifier, we just initialize `rf_clf = RandomForestClassifier(n_jobs = -1, n_estimators = 50)`
The n_jobs parameter is how many jobs to run in parallel. - fit - predict - decision_path - path
`n_jobs = -1` means to use all processors

## The n_estimators is how many trees to have in the forest

**Predicting using it**
The Random Forest Classifier has a **fit()** function which takes in two inputs.

1. Collection of feature variables
   - A feature variable is a set of variables we look at to determine the target
2. Target variable
   - A target variable is a variable we want to predict
