# Polynomial Regression

This notebook demonstrates the implementation of **Polynomial Regression** using Python and Scikit-learn.

## 📌 What is Polynomial Regression?

Polynomial Regression is a supervised machine learning algorithm used to model the relationship between an independent variable and a dependent variable using a polynomial equation.

Unlike Linear Regression, which fits a straight line, Polynomial Regression can fit a curved relationship between variables.

The general form is:

[
y = b_0 + b_1x + b_2x^2 + b_3x^3 + \cdots + b_nx^n
]

Where:

* `y` → Predicted output
* `x` → Input feature
* `b₀` → Intercept
* `b₁, b₂, ..., bₙ` → Model coefficients
* `n` → Degree of the polynomial

## 🎯 Objective

The goal of this notebook is to:

* Understand the concept of Polynomial Regression.
* Generate and visualize nonlinear data.
* Transform features into polynomial features.
* Train a Polynomial Regression model.
* Make predictions.
* Visualize the polynomial regression curve.
* Compare the model's predictions with actual data.

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

## 🔄 Workflow

```text
Create or Load Data
        ↓
Visualize the Data
        ↓
Create Polynomial Features
        ↓
Train the Regression Model
        ↓
Make Predictions
        ↓
Evaluate the Model
        ↓
Visualize the Polynomial Curve
```

## 📚 Main Concepts

### 1. Polynomial Features

Polynomial features transform the original feature into higher-degree features.

For example, if the degree is `2`:

```text
x → x, x²
```

If the degree is `3`:

```text
x → x, x², x³
```

This allows a linear regression model to learn nonlinear relationships.

### 2. Polynomial Regression Pipeline

A typical Polynomial Regression workflow is:

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

model = make_pipeline(
    PolynomialFeatures(degree=2),
    LinearRegression()
)
```

### 3. Model Prediction

After training the model:

```python
model.fit(X, y)

y_pred = model.predict(X)
```

## 📊 Visualization

The notebook visualizes:

* Original data points.
* The fitted Polynomial Regression curve.
* The relationship between the input feature and target variable.

Polynomial Regression is useful when the relationship between variables is **curved rather than strictly linear**.

## ⚠️ Choosing the Polynomial Degree

The polynomial degree affects the model's complexity:

| Degree        | Model Behavior      |
| ------------- | ------------------- |
| 1             | Linear relationship |
| 2             | Quadratic curve     |
| 3             | Cubic curve         |
| Higher degree | More complex curve  |

A very low degree can cause **underfitting**, while a very high degree can cause **overfitting**.

## 📂 Repository Structure

```text
Polynomial Regression Simple/
│
├── Polynomial Regression Simple.ipynb
└── README.md
```

## 🚀 Conclusion

Polynomial Regression extends Linear Regression by adding polynomial features to model nonlinear relationships. It is a useful technique when a straight line is not sufficient to accurately represent the relationship between the input and output variables.

