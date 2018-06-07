import pandas as pd
import os

#import California Housing Data as Dataframe
dir_path = os.path.dirname(os.path.realpath(__file__))
california_housing_dataframe = pd.read_csv(os.path.join(dir_path,'california_housing_train.csv'))
print(california_housing_dataframe.describe())
print(california_housing_dataframe.head())
