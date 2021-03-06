import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

# ## Load in data with `read_csv()` 
data = pd.read_csv("iris.csv")


print ("These are some summary statistics for the iris DataFrame: \n")
data.describe()

print ("These are some summary statistics for the iris DataFrame: \n")
data.info()

# Used to give user info on the first 10/last 10 results in dataset: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html

print ("These are the first 10 and last 10 results in the dataset: \n")
data.head(10)
data.tail(10)

#I then adapted this code from stackoverflow - https://stackoverflow.com/questions/41428539/data-frame-to-file-txt-python
data.to_csv('iris.txt', sep='\t', index=False)
#This then writes the data to a text file


#Part 2 - Developing Histograms

## I used this as the basis for my code = https://towardsdatascience.com/matplotlib-tutorial-with-code-for-pythons-powerful-data-visualization-tool-8ec458423c5e
#Loads in dataset - More info provided here - https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html

iris = datasets.load_iris()
##This loads in the dataset from sklearn 
X_iris = iris.data

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
## I amended the figsize to specify the width and height of the figure, as I found a lot of the data was coming together
axs[0, 0].hist(X_iris[:, 0])
axs[0, 1].hist(X_iris[:, 1], color='orange')
axs[1, 0].hist(X_iris[:, 2], color='green')
axs[1, 1].hist(X_iris[:, 3], color='red')
## This allows each graph to have a different colour, blue is by default.

i = 0
for ax in axs.flat:
    ax.set(xlabel=iris.feature_names[i], ylabel='Frequency')
    i += 1
#This adds the "frequency" label to the Y column

fig.suptitle("Iris Histograms")
##Puts Title at the top of piece

plt.savefig('IrisHistogram.png', bbox_inches="tight")
#Plots the figure into a histogram for the user
#I found the x Column was clashing with column on lower table and added in bbox-inches to prevent - https://matplotlib.org/3.5.0/tutorials/intermediate/tight_layout_guide.html#


#3. Scatterplot of the Iris Data Set

#I used this as the basis for my solution - https://seaborn.pydata.org/examples/scatterplot_matrix.html
sns.set_theme(style="whitegrid")
#There are 5 inbuilt seaborn types, I decided to use "whitegrid" as I thought it looked best for solution = https://seaborn.pydata.org/tutorial/aesthetics.html
df = sns.load_dataset("iris")
#Iris has an inbuilt dataset for Iris
sns.pairplot(df, hue="species")
#I used the default here on code as it seemed to be the best, also
plt.savefig('IrisScatterplot.png')
#This then gets output to the user, it is currently saving in same folder as I have my code in.


#4. Correlation Methods to be used.

#Solution I am using is adapted from this example - https://www.geeksforgeeks.org/python-pandas-dataframe-corr/

# To find the correlation among the columns using pearson method
print("Pearson Method")
print(df.corr(method ='pearson'))
print("")
#Added to put a space between the data

# To find the correlation among the columns using pearson method
print("Kendall Method")
print(df.corr(method ='kendall'))
print("")

# To find the correlation among the columns using pearson method
print("Spearman Method")
print(df.corr(method ='spearman'))
print("")
