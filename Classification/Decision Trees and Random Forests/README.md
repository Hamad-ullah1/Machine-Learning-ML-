# Decision Trees and Random Forests

This folder contains learning materials and implementations of two important **supervised machine learning algorithms**: **Decision Trees** and **Random Forests**.

## 🌳 Decision Trees

A **Decision Tree** is a supervised machine learning algorithm that makes predictions by asking a series of questions about the features and following decision rules until reaching a final prediction.

### Example

```text
Is Age > 30?
├── Yes → Class A
└── No  → Class B
```

Decision Trees can be used for:

* Classification
* Regression

## 🌲 Random Forests

A **Random Forest** is an ensemble learning algorithm that combines multiple Decision Trees to make more accurate and reliable predictions.

Instead of relying on a single tree:

```text
Decision Tree 1 → Class A
Decision Tree 2 → Class A
Decision Tree 3 → Class B
Decision Tree 4 → Class A

Final Prediction → Class A
```

The final prediction is usually based on the majority vote of the individual trees.

## 📚 Topics Covered

* Decision Tree Classification
* Decision Tree Regression
* Random Forest Classification
* Random Forest Regression
* Model Training and Prediction
* Feature Importance
* Model Evaluation

## 🛠️ Libraries Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

## 🎯 Learning Objectives

By studying these algorithms, you will learn:

* How Decision Trees make predictions
* How trees split data using features
* How Random Forests combine multiple Decision Trees
* The difference between a single Decision Tree and a Random Forest
* How to train and evaluate tree-based models
* How to analyze feature importance

## 📂 Folder Structure

```text
Decision Trees and Random Forests/
│
├── Decision Tree Classification/
├── Decision Tree Regression/
├── Random Forest Classification/
├── Random Forest Regression/
└── README.md
```

## 📌 Conclusion

**Decision Trees** are simple and interpretable models that make predictions using decision rules. **Random Forests** combine multiple Decision Trees to improve prediction performance and reduce overfitting.

Both algorithms are widely used in **Machine Learning** for classification and regression tasks.

