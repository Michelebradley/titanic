import json
import requests
import os

with open('kaggle.json') as json_file:
    kaggle_us_pw = json.load(json_file)

os.environ['KAGGLE_USERNAME'] = list(kaggle_us_pw.values())[0]
os.environ['KAGGLE_KEY'] = list(kaggle_us_pw.values())[1]

os.system('kaggle competitions download -c "titanic"')