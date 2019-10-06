import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
import zipfile

#Import data after running pull_data.py from the command line
zf = zipfile.ZipFile('titanic.zip') 
test = pd.read_csv(zf.open('test.csv'))
train = pd.read_csv(zf.open('train.csv'))

"""
The competition is simple: use machine learning to create a model that predicts which passengers survived the Titanic shipwreck.
This is a classification machine learning problem, in which case the computer program is asked to determine which of k categories some input will fall into.

The Performance Measure evaluates the ability of the machine learning algorithm. In this instance, we have the output of the algorithm and can test how accurate our code is.

We often measure the accuracy of the model, to see what proportion of examples were correct (calcuated via the error rate, or proportion of examples that were incorrect).

This is a supervised learning algorithm, in which each example is associated with a label.
"""

#Clean Data to use those that appear to have difficant implications on survival

#use first character of Cabin Variable
def first_char(df, column):
  df[column] = df[column].astype(str).str[0]
  return df

train = first_char(train, 'Cabin')
test = first_char(test, 'Cabin')

#update string values to float
def string_to_float(df, column, val1, val2):
  df[column][df[column] == val1] = 1
  df[column][df[column] == val2] = 0
  return df

train = string_to_float(train, 'Sex', 'male', 'female')
test = string_to_float(test, 'Sex', 'male', 'female')

#update characters to float
def char_to_float(df, column):
  df[column] = df[column].transform(lambda x: ord(x))
  return df

train = char_to_float(train, 'Cabin')
test = char_to_float(test, 'Cabin')

#determine size of family
def family(df):
  df['Family'] = df['SibSp'] + df['Parch']
  return df

train = family(train)
test = family(test)

#imput null values with a mean
def mean_impute(df, column):
  df[column] = df[column].transform(lambda x: x.fillna(x.mean()))
  return df
  
train = mean_impute(train, 'Age')
test = mean_impute(test, 'Age')

train = mean_impute(train, 'Fare')
test = mean_impute(test, 'Fare')

train = train.drop(['Embarked', 'PassengerId', 'Name', 'Ticket'], axis=1)
test = test.drop(['Embarked', 'PassengerId', 'Name', 'Ticket'], axis=1)

#run random forest model
rf = RandomForestClassifier(criterion='gini', 
                             n_estimators=700,
                             min_samples_split=10,
                             min_samples_leaf=1,
                             max_features='auto',
                             oob_score=True,
                             random_state=1,
                             n_jobs=-1)
rf.fit(train.iloc[:, 1:], train.iloc[:, 0])

pkl_filename = "model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(rf, file)

test.to_csv('test_modified.csv', index = False)