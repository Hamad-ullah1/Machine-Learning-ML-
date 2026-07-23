# Support Vector Machines (SVM)

This folder contains learning materials and implementations of **Support Vector Machines (SVM)**, a powerful supervised machine learning algorithm used for classification and regression.

## 📌 What is SVM?

**Support Vector Machine (SVM)** is a supervised machine learning algorithm that finds the best decision boundary, called a **hyperplane**, to separate different classes of data.

The best boundary is the one that creates the **maximum margin** between the classes.

### Example

```text
Class A  ● ● ●  |  ○ ○ ○  Class B
                  ↑
            Decision Boundary
```

The data points closest to the decision boundary are called **Support Vectors**.

## 📚 Topics Covered

* Introduction to Support Vector Machines
* Hyperplanes
* Decision Boundaries
* Support Vectors
* Maximum Margin
* Linear SVM
* Non-Linear SVM
* Kernel Trick
* Common Kernel Functions
* SVM Classification
* Model Training and Prediction
* Model Evaluation

## 🧠 Important Concepts

### Support Vectors

The data points closest to the decision boundary that help determine the position of the boundary.

### Margin

The distance between the decision boundary and the closest data points from each class.

### Kernel Trick

A technique that allows SVM to handle non-linear data by transforming it into a higher-dimensional space.

Common kernels include:

* Linear
* Polynomial
* RBF
* Sigmoid

## 🛠️ Libraries Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

## 🎯 Learning Objectives

By studying SVM, you will learn:

* How SVM separates different classes
* What a hyperplane is
* How support vectors determine the decision boundary
* How SVM maximizes the margin
* How SVM handles non-linear data
* How kernel functions work
* How to train and evaluate an SVM model

## 📂 Folder Structure

```text
Support Vector Machines/
│
├── Introduction to SVM/
├── Hyperplanes and Decision Boundaries/
├── Support Vectors and Margins/
├── Linear SVM/
├── Non-Linear SVM/
├── Kernel Trick/
├── SVM Classification/
├── Model Training and Prediction/
├── Model Evaluation/
└── README.md
```

## 📌 Conclusion

**Support Vector Machines** are powerful machine learning algorithms that find the best boundary for separating classes. They are especially useful for high-dimensional data and can handle both linear and non-linear classification problems using kernel functions.

