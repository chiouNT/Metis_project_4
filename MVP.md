Minimum Viable Product (Ni-Ting Chiou)

##  Identifying mis-classified ClinVar variants
* **Goal:** Many human genome variants have conflicting classification in the ClinVar database. Predicting whether a variant is likely to be classified into the conflicting class will help biologist to design the strategies for improving their annotations.
* **Process:** The dataset was obtained via Kaggle and is comprised of over 60K observations and 45 features. 8 promising features (3 of them are numeric and 5 of them are categorical features) were selected. For these features, the categorical features were converted into dummy variables and numeric features were standardized for modeling.
* **Preliminary conclusion:** The preliminary classification analysis is done with Logistic Regression and Random Forest models. The ROC-AUC curves show that a tree-based model may be better for identifying mis-classified ClinVar variant.
* **From here:** More EDA will be done for feature selection and engineering to improve model scoring metrics.





![alt text](https://github.com/chiouNT/Classification/blob/main/Images/ROC.png)
