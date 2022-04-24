### Kenneth Linehan, 2022

## Introduction

This is my analysis into the [Fisher's Iris Data Set](http://archive.ics.uci.edu/ml/datasets/Iris), using the python language.


## What is the Data Set?

# Overview on Dataset

The Iris Dataset contains four features (length and width of sepals and petals) of 50 samples of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). These measures were used to create a linear discriminant model to classify the species. The dataset is often used in data mining, classification and clustering examples and to test algorithms.

This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. [1]

Predicted attribute: class of iris plant.

Attribute Information:

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica

## Brief History

The first main study was by Edgar Anderson whom collected data on 3 different irise species on the Gaspé Peninsula, Quebec, Canada. Anderson collected the data in a journal which is called The Irises of the Gaspe Peninsula which was published in October 1935. This data was the start of the analyis data sets. Fisher has cited the "Iris versicolor and Iris virginica were chosen for such a
study since they customarily grow in colonies containing many individual plants ; a peculiarity which facilitates the location and study of large numbers of individuals." [2] 

Ronald Fisher would then build on the research completed by Anderson. Fisher used
Anderson’s data to see if linear regression could be used to could be used to “maximize the ratio of the
difference between the specific means to the standard deviations within species.” [3]




## Data Set Analysis

I firstly have added IRIS.csv to the repository as this is the raw data used.

I also added a version of the same file in a read me file in order to view the raw data. Please see link to data here - (https://github.com/KenLin765/pands-project/blob/main/iris.md)

A link to the dataset can also be found here - https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data


This data is separated into 5 main columns with the data included. These headings are sepal_length,  sepal_width, petal_length, petal_width, and species.




## Iris Dataset Data Analysis

I will be using exploratory data analysis(EDA) alongside Python to investigate the dataset. 

John Tukey has defined EDA as the following; 

The term “Exploratory Data Analysis” was introduced by John W. Tukey who shows how simple graphical and quantitative techniques can be used to open-mindedly explore data.

Typical graphical techniques are
1. Plotting the raw data (e.g., stem-and-leaf diagrams, histograms, scatter plots)
2. Plotting simple statistics (e.g., mean plots, box plots, residual plots)
3. Positioning (multiple) plots to amplify cognition

Typical quantitative techniques are
1. Interval estimation
2. Measures of location or of scale
3. Shapes of distributions

Exploratory data analysis can help to improve the results of statistical hypothesis testing. [4]

Please see link to code used here (https://github.com/KenLin765/pands-project/blob/main/analysis.py)






References Used
[1] UCI Machine Learning Repository - Iris dataset - https://archive.ics.uci.edu/ml/datasets/iris

[2] Edgar Anderson, The irises of the Gasp´e Peninsula, Bulletin of
the American Iris society 59 (1935), 2–5 - https://wiki.irises.org/pub/Hist/Info1986SIGNA37/SIGNA_37.pdf

[3] Ronald A Fisher,
The Use of Multiple Measurements in Taxonomic Problems, Annals of Eugenics 7 (1936), no. 2, 179–188. - http://syllabus.cs.manchester.ac.uk/pgt/2021/COMP61021/reference/Fisher-DA.pdf

[4] John Tukey, Exploratory Data Analysis http://theta.edu.pl/wp-content/uploads/2012/10/exploratorydataanalysis_tukey.pdf