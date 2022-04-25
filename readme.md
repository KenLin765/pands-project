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


## Investigating data set using dataframe 

In reviewing many different sources online, such as Mittapaldi, 2018[5] Carpenter, 2020[6], many different people have first described the dataset and general information around the dataset using Pandas. 

I firstly read in the data of the iris.csv file and used pandas to describe the data. The file is located in the same folder as my python file. Pandas allows us to see that the dataset is comprised of 150 rows and 5 columns. It also allow us to see stats such as a count of the data, mean, median and mode. This describes the dataset at a very high level. These could also be described individually with iris.mean() or iris.min()

The main findings are as follows:

*There are 150 rows and 5 columns of data.

*On the table we see the column headers of, Length of the sepal, the length of the petal, the width of the sepal and the width of the petal which is recorded in centimetres.

*All forms of measurement such as the mean, of the Sepal length is greater than the mean of the other three values in the column.

*Petal width has the lowest average value of all the measurements.

*The smallest petal is 1 cm, the longest petal is 6.9 cm.

*The widths of the petals vary between 0.1 cm to 2.5 cm.

*The smallest sepal in the data set is 4.3 cm, the longest sepal is 7.9 cm.

*The narrowest sepal is 2cm, the widest sepal is 4.4 centimetres.

![Iris Describe](https://github.com/KenLin765/pands-project/blob/main/iris_describe.png)



I then ran the info dataframe which us with a bit more information on the dataset.

The main findings are as follows:

*There are 150 entries within the range index

*This indicates there are 5 columns

*These columns consist of number, Column(name), Non-Null, Count and Dtype

*# is used as a count to show number of entry

*Column defines the values which are sepal.length, sepal.width, petal.length, petal.width and variety

*Non-Null instructs a column to not accept null values

*The Range-Index has 150 entries from 0 to 149

*The four measurement columns each consist of 149 non-null float64 numbers with the last one being an object datatype that contains the species names.

![Iris Info](https://github.com/KenLin765/pands-project/blob/main/iris_info.png)


I then ran the data.head and data.tail Pandas as this gives quick observations of the data displayed.

The rows at the top belong to the Iris Setosa class, the data is ordered in this way when you download the csv file.

![Iris Head](https://github.com/KenLin765/pands-project/blob/main/Iris_head.png)



## Plotting the Data

I am firstly plotting the data using histograms. The histograms show the distribution of each of the measurement attributes across the iris data set. I used the the matplotlib - pyplot package to create the histogram. I then also used [scikit](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html), to help plot the data as this software included inbuilt data which makes it useful to plot the data. It would also be possible to plot each data separately but I decided to include all data in one. The data for the user will then display in a .png file format.

The main findings based on this data are that the sepal length for the most part is about double the size of the sepal width while the petal length is also approximately 2 and a half times the size in cm of the petal width. 

*The Highest frequency of sepal width is between 3.0 to 3.5.
*The Highest frequency of sepal length is between 5.5 and 6.5.
*The Highest frequency of petal width is more changable than the others and spikes at 0 and 1.5
*The Highest frequency of petal length is between 0 to 0.5.

![Iris Histogram](https://github.com/KenLin765/pands-project/blob/main/IrisHistogram.png)



References Used
[1] UCI Machine Learning Repository - Iris dataset - https://archive.ics.uci.edu/ml/datasets/iris

[2] Edgar Anderson, The irises of the Gasp´e Peninsula, Bulletin of
the American Iris society 59 (1935), 2–5 - https://wiki.irises.org/pub/Hist/Info1986SIGNA37/SIGNA_37.pdf

[3] Ronald A Fisher,
The Use of Multiple Measurements in Taxonomic Problems, Annals of Eugenics 7 (1936), no. 2, 179–188. - http://syllabus.cs.manchester.ac.uk/pgt/2021/COMP61021/reference/Fisher-DA.pdf

[4] John Tukey, Exploratory Data Analysis http://theta.edu.pl/wp-content/uploads/2012/10/exploratorydataanalysis_tukey.pdf

[5] Hari Mittapalli, Exploratory Data Analysis : Iris DataSet - https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset-9920ea439a3e

[6] Angela Carpenter, Investigating the Iris dataset - https://www.angela1c.com/projects/iris_project/investigating-the-iris-dataset/