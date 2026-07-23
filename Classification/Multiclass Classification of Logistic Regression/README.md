# Multiclass Classification with Logistic Regression

This folder contains learning materials and implementations of **Multiclass Classification using Logistic Regression**.

## 📌 What is Multiclass Classification?

**Multiclass Classification** is a classification problem where the model predicts one class from **more than two possible classes**.

### Example

```text id="3z5m5f"
Class 0 → Cat
Class 1 → Dog
Class 2 → Bird
```

The model predicts which one of these classes the input belongs to.

## 🔄 Logistic Regression for Multiclass Classification

Although Logistic Regression is commonly used for binary classification, it can also handle multiple classes using strategies such as:

* **One-vs-Rest (OvR)**
* **Multinomial Logistic Regression**

### Example

For three classes:

```text id="w5l2v9"
Class 0 → Model 1
Class 1 → Model 2
Class 2 → Model 3
```

The model calculates probabilities for each class and selects the class with the highest probability.

## 📚 Topics Covered

* Multiclass Classification
* Logistic Regression for Multiple Classes
* One-vs-Rest (OvR)
* Multinomial Logistic Regression
* Probability Estimation
* Class Prediction
* Model Evaluation

## 🛠️ Libraries Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

## 🎯 Learning Objectives

By studying this topic, you will learn:

* The difference between binary and multiclass classification
* How Logistic Regression handles multiple classes
* How One-vs-Rest works
* How class probabilities are calculated
* How the final class is selected
* How to train and evaluate a multiclass classification model

## 📂 Folder Structure

```text id="3b3qk3"
Multiclass Classification of Logistic Regression/
│
├── Multiclass Classification/
├── One-vs-Rest/
├── Multinomial Logistic Regression/
├── Model Training and Prediction/
├── Model Evaluation/
└── README.md
```

## 📌 Conclusion

**Multiclass Classification with Logistic Regression** is used when the target variable contains more than two possible classes. Logistic Regression can calculate the probability of each class and select the class with the highest probability.

