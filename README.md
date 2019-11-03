DATA 622 # hw2

	Assigned on September 15, 2018
	Due on October 6, 2019 11:59 PM EST
	17 points possible, worth 17% of your final grade

1. Required Reading

  Read Chapter 4 of the Deep Learning Book
	Read Chapter 5 of the Deep Learning Book
	Read Chapter 1 of the Agile Data Science 2.0 textbook

2. Data Pipeline using Python (13 points total)

	Build a data pipeline in Python that downloads data using the urls given below, trains a random forest model on the training dataset using sklearn and scores the model on the test dataset.

	Scoring Rubric

	The homework will be scored based on code efficiency (hint: use functions, not stream of consciousness coding), code cleaniless, code reproducibility, and critical thinking (hint: commenting lets me know what you are thinking!)
Instructions:

	Submit the following 5 items on github.
	ReadMe.md (see "Critical Thinking")
	requirements.txt
	pull_data.py
	train_model.py
	score_model.py

More details:

requirements.txt (2 point)
This file documents all dependencies needed on top of the existing packages in the Docker Dataquest image from HW1. When called upon using pip install -r requirements.txt , this will install all python packages needed to run the .py files. (hint: use pip freeze to generate the .txt file)

pull_data.py (5 points)
When this is called using python pull_data.py in the command line, this will go to the 2 Kaggle urls provided below, authenticate using your own Kaggle sign on, pull the two datasets, and save as .csv files in the current local directory. The authentication login details (aka secrets) need to be in a hidden folder (hint: use .gitignore). There must be a data check step to ensure the data has been pulled correctly and clear commenting and documentation for each step inside the .py file.
	Training dataset url: https://www.kaggle.com/c/titanic/download/train.csv
	Scoring dataset url: https://www.kaggle.com/c/titanic/download/test.csv

train_model.py (5 points)
When this is called using python train_model.py in the command line, this will take in the training dataset csv, perform the necessary data cleaning and imputation, and fit a classification model to the dependent Y. There must be data check steps and clear commenting for each step inside the .py file. The output for running this file is the random forest model saved as a .pkl file in the local directory. Remember that the thought process and decision for why you chose the final model must be clearly documented in this section.
eda.ipynb (0 points)

[Optional] This supplements the commenting inside train_model.py. This is the place to provide scratch work and plots to convince me why you did certain data imputations and manipulations inside the train_model.py file.

score_model.py (2 points)
When this is called using python score_model.py in the command line, this will ingest the .pkl random forest file and apply the model to the locally saved scoring dataset csv. There must be data check steps and clear commenting for each step inside the .py file. The output for running this file is a csv file with the predicted score, as well as a png or text file output that contains the model accuracy report (e.g. sklearn's classification report or any other way of model evaluation).

3. Critical Thinking (3 points total)
Modify this ReadMe file to answer the following questions directly in place.
	1) Kaggle changes links/ file locations/login process/ file content
	
		a) Kaggle changes links: Should not have an effect since using kaggle api. Their website link does not matter.
		
		b) Kaggle changes file locations: Modify line if "titanic" file name changes os.system('kaggle competitions download -c "titanic"')
		
		c) Kaggle change login process: Modify pull_data.py if the API login process changes
		
		d) Kaggle changes file content: Depends on what changes. If file name changes, we have to modify the names that are being pulled in train_model.py and score_model.py. If column name changes, then changes become more complex.

	2) We run out of space on HD / local permissions issue - can't save files: 
	
	Use instead, a cloud based service, such as Google Collab.
	
	3) Someone updated python packages and there is unintended effect (functions retired or act differently): 
	
	Modifications will take time. Will need to update the requirements.txt file as well as any functions that are causing complications.

	4) Docker issues - lost internet within docker due to some ip binding to vm or local routing issues( I guess this falls under lost internet, but I am talking more if docker is the cause rather then ISP):
	
	Docker issues might require re-building or encouraging use of code in local environment from github.
"# titanic" 
