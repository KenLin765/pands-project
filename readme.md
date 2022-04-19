### Kenneth Linehan, 2022

## Introduction

This is my analysis into the [Fisher's Iris Data Set](http://archive.ics.uci.edu/ml/datasets/Iris), using the python language.


## What is the Data Set?

# Brief History 

The Iris Dataset contains four features (length and width of sepals and petals) of 50 samples of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). These measures were used to create a linear discriminant model to classify the species. The dataset is often used in data mining, classification and clustering examples and to test algorithms.[1]


The first main study was by Edgar Anderson whom collected data on 3 different irise species on the Gaspé Peninsula, Quebec, Canada. Anderson collected the data in a journal which is called The Irises of the Gaspe Peninsula which was published in October 1935. This data was the start of the analyis data sets. Fisher has cited the "Iris versicolor and Iris virginica were chosen for such a
study since they customarily grow in colonies containing many individual plants ; a peculiarity which facilitates the location and study of large numbers of individuals." [2] 

Ronald Fisher would then build on the research completed by Anderson. Fisher used
Anderson’s data to see if linear regression could be used to could be used to “maximize the ratio of the
difference between the specific means to the standard deviations within species.” [3]


# UCI Definition of the data:

This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other.

Predicted attribute: class of iris plant.

This is an exceedingly simple domain.

This data differs from the data presented in Fishers article (identified by Steve Chadwick, spchadwick '@' espeedaz.net ). The 35th sample should be: 4.9,3.1,1.5,0.2,"Iris-setosa" where the error is in the fourth feature. The 38th sample: 4.9,3.6,1.4,0.1,"Iris-setosa" where the errors are in the second and third features.


Attribute Information:

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica













References Used
[1] UCI Machine Learning Repository - Iris dataset - https://archive.ics.uci.edu/ml/datasets/iris

[2] Edgar Anderson, The irises of the Gasp´e Peninsula, Bulletin of
the American Iris society 59 (1935), 2–5 - https://wiki.irises.org/pub/Hist/Info1986SIGNA37/SIGNA_37.pdf

[3] Ronald A Fisher,
The Use of Multiple Measurements in Taxonomic Problems, Annals of Eugenics 7 (1936), no. 2, 179–188. - http://syllabus.cs.manchester.ac.uk/pgt/2021/COMP61021/reference/Fisher-DA.pdf