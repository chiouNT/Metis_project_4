write_up (Ni-Ting Chiou)

# Classification models to predict whether a variant will have conflicting clinical classifications.

## Abstract

The DNA sequences within the human cells have many variants, which lead to different human tracts as well as diseases. Many human genome variants have conflicting classification in the ClinVar database. Predicting whether a variant is likely to be classified into the conflicting class will help biologists to design the strategies for improving their annotations.

## Design

The variants in the Clinvar database are manually classified by labs into 3 categories: (1) likely benigh or benigh, (2) VUS (variants of uncertain significance) (3) likely pathogenic or pathogenic. When 2 of these 3 categories are present for one variant, this variant is classified as conflicting class.  The objective is to predict whether a ClinVar variant will have conflicting classification.

## Data

The data (ClinvarClassification.csv) is downloaded from Kaggle. The data has 65188 variants with 46 features. Among these features, some of them have >90% null values, and some of them are redundant. For the rest of features, the numerical features were analyzed by pairplot and categorical features were analyzed by Chi2 test. Based on the analysis, the features that were not different among the 2 classes (non-conflicting vs conflicting class) were removed. Finally, the data used for model fitting has 8 features.  

## Algorithms

* Feature Engineering
1.  Bucketing the minority categorical variants under one feature into a single category.
2.	Converting categorical features into the dummy variables.
3.	Combing the dummies and numerical features 
4.	Standardizing the final data

* Models <br>
Logistic regression, k-nearest neighbors, random forest classifiers and XGBoost Classifier were used before settling on XGBoost Classifier as the model with best scores.

*Final Model Evaluation* <br>
* Accuracy 0.76
* F1 0.19
* precision 0.66
* recall 0.11

*Holdout* <br>
* Accuracy 0.75
* F1 0.18
* precision 0.59
* recall 0.11

## Tools
*	Pandas, Numby, Matplotlib and Seaborn: Data clean, exploration and visualization
*	Sci-learn learn: predictive data analysis and evaluation


## Communication
* The analysis result showed that the features of variant frequency, gene name and molecular consequences are more important for predicting whether a variant will have conflicting classification (see figure bellow)

![alt text](https://github.com/chiouNT/Classification/blob/main/Images/importance.png)

