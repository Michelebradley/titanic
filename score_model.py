import pickle
import pandas as pd
import zipfile
import numpy as np
from sklearn.metrics import classification_report

test = pd.read_csv('test_modified.csv')

# Load from file
with open('model.pkl', 'rb') as file:
    pickle_model = pickle.load(file)
    
# Calculate the accuracy score and predict target values
predictions = pickle_model.predict(test)
predictions = pd.DataFrame(predictions, columns=['Survived'])

zf = zipfile.ZipFile('titanic.zip') 
test = pd.read_csv(zf.open('test.csv'))
my_predictions = pd.concat((test.iloc[:, 0], predictions), axis = 1)
my_predictions['pred'] = my_predictions['Survived']

results = pd.read_csv(zf.open('gender_submission.csv'))
p = pd.concat((my_predictions, results), keys=['PassengerId'], axis = 1)

p.to_csv('predictions.csv')

y_true = my_predictions['pred'] 
y_pred = results['Survived']

print(classification_report(y_true, y_pred))