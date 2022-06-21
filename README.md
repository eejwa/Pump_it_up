# Sentiment Analysis of Climate Related Tweets

This notebook and associated python files takes information about water pumps in Tanzania and classifies them as either functional, non-functional or functional needs repair. In addition to this task, I thought it would be valuable to know how important the information is. Knowing the relative value of the data can then be used for a more targetted survey in the future and waste less time in the data collection period. 

## Data

Raw data is provided in the *csv files which are then preprocessed in the notebook. For full details on the data and the background of their collection see here: https://www.kaggle.com/datasets/tatianasnwrt/pumpitup-challenge-dataset

## Files

- Classification_Broken_Pump.ipynb: ipython notebook where the raw data is preprocessed, multiple machine learning models are trained on the data and inferences are calculated using random forests. Reflection on the data and the processing is given throughout.

- plotting.py: holds functions to plot stations. 

- preprocessing.py: holds functions to preprocess data and extract feature names. 

- testing_classifiers.py: holds functions to test the classifiers and plot their performance. 

## Use

To use this notebook and files, you need to download the data from the link above and install the anaconda environment provided using: 

`conda env create -f environment.yml`

then you can open up the notebook either in visual studio code or in a jupyter notebook. 


