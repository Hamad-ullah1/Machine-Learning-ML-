# Logistic Regression

This folder contains learning materials and implementations of **Logistic Regression**, a supervised machine learning algorithm used for classification problems.

## 📌 What is Logistic Regression?

**Logistic Regression** is a supervised machine learning algorithm used to predict the probability of a categorical outcome.

Unlike Linear Regression, which predicts continuous values, Logistic Regression predicts the probability of a class, such as:

```text
0 → No
1 → Yes
```

The predicted probability is converted into a class using a **classification threshold**, commonly `0.5`.

## 📚 Topics Covered

* Introduction to Logistic Regression
* Probability Estimation
* Sigmoid Function
* Cost Function
* Decision Boundaries
* Visualizing Decision Boundaries
* Decision Boundary Equation
* Visualizing the Dataset
* Model Evaluation
* Decision Tree Classification

## 📈 Example

Suppose we want to predict whether a customer will purchase a product:

```text
Age = 25
Salary = 50000
```

The model may predict:

```text
Probability = 0.82
```

If the threshold is `0.5`:

```text
0.82 >= 0.5 → Purchased = 1 (Yes)
```

## 🛠️ Libraries Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

## 🎯 Learning Objectives

By studying Logistic Regression, you will learn:

* How Logistic Regression performs classification
* How probabilities are estimated
* How the Sigmoid Function works
* How the Cost Function is used
* How Decision Boundaries separate classes
* How to visualize classification results
* How to evaluate a classification model

## 📂 Folder Structure

```text
Logistic Regression/
│
├── Introduction to Logistic Regression/
├── Probability Estimation/
├── Sigmoid Function/
├── Cost Function/
├── Decision Boundaries/
├── Visualizing Decision Boundaries/
├── Decision Boundary Equation/
├── Visualizing the Dataset/
├── Model Evaluation/
└── README.md
```

## 📌 Conclusion

**Logistic Regression** is one of the most important classification algorithms in Machine Learning. It is commonly used for binary classification problems and provides both a predicted class and the probability of that class.

