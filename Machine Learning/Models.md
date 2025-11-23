# Models

## Introduction

    Machine Learning models can be divided into tow categories which are as follows:
    
        1. Supervised Learning
        2. Unsupervised Learning

### Supervised Learning

    It involves a series of functions which maps an input to an output based on series of examples input output pairs.
    
    We have two types of supervised machine learning modes:
    
        1. Regression
        2. Classification

#### Regression

    In regression model we try to find a target value based on independent predictors that means we can find relationship between dependent variable and independent variables.
    The values generated with the regression model is continuos.
    
    Types of regression models are as follows:
       
        1. Linear Regression:
                The method to simply find a line which fits the data and it has multiple variants like multiple linear regression (finding a plane for best fit) and polynomials (finding a curve for best fit)
        
        2. Decision Tree
                A feature based node tree more depth it has more accurate the results are.
        
        3. Random Forests
                Ensemble learning techniques which uses decision trees as a base and uses many of the DT using bootstrap datasets of original dataset then it randomly selects a subset of variables at each step of the DT.
                Then it takes the mode of all DTs and process everything under majority win rules.
        
        4. Neural Networks
                A multi layer network inspired by our brain.
                it has nodes and layers as a primary elements.
                it has input layer, hidden layer and output layer.

#### Classification

    The output for classification is always discrete.
    
    There are many types of classifications algorithms which are as follows:
    
       1. Logistic Regression
                similar to linear regression but is used to model the probability of a finite number of outcast, typically 2 i.e. o or 1.
    
       2. Support Vector Machine
                Used to find a hyperplane in n-dimensional space that can distinctly classify data points.
    
       3. Naive Bayes
                This algo acts as a probabilistic machine learning model used for classification tasks the crux of the classifier is based on the bayes theorem.
    
       4. Decision Trees, Random Forest, Neural Networks
                These are same model but the output are discrete.

### Unsupervised Learning

    A machine learning technique which is used to draw inferences and find patterns from the input data without reference to the labeled outcome.
    
    Types of unsupervised machine learning are as follows:
    
        1. Clustering
        2. Dimensionality Reduction

#### Clustering

    Grouping of data points is known as clustering.
    it is used for customer segmentation, probe detection and document classification.

    Types of clustering techniques:
    
        1. K-means
        2. Hierarchical
        3. Mean Shift
        4. Density-based

#### Dimensionality Reduction

    A process of reducing dimensions of your feature set i.e. reducing the number of features.
    
    Types of dimensionality reduction:
    
        1. Feature Elimination
        2. Feature Extraction

    Most common technique: Principal Component Analysis (PCA).
