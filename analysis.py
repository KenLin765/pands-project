import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# This is used to read in the data:
data = pd.read_csv("iris.csv")

print ("These are some summary statistics for the iris DataFrame: \n")
data.describe()

print ("These are some summary statistics for the iris DataFrame: \n")
data.info()

# Used to give user info on the first 10/last 10 results in dataset: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html

print ("These are the first 10 and last 10 results in the dataset: \n")
print(data.head(10))
print(data.tail(10))