# Univariate Linear Regression and Gradient Descent

This project demonstrates **Univariate Linear Regression** and the **Gradient Descent optimization algorithm** using Python and NumPy.

The model is implemented step by step to understand how a linear regression model learns the relationship between one input feature and one target variable.

## 📌 What is Univariate Linear Regression?

Univariate Linear Regression predicts a target variable using **one independent feature**.

The model learns a straight-line relationship between `X` and `y`.

For example:

```text
X → Input Feature
y → Target Variable
```

The model learns:

* **Weight (w₁)** → Controls the slope of the line.
* **Bias (w₀)** → Controls the intercept.

The model uses the learned parameters to generate predictions.

## 🎯 Objective

The goal of this notebook is to understand the complete process of training a linear regression model from scratch:

* Create a synthetic dataset.
* Add random noise to simulate real-world data.
* Visualize the data.
* Standardize the features.
* Split the data into training and testing sets.
* Initialize model parameters.
* Generate predictions using a hypothesis function.
* Calculate the cost function.
* Optimize parameters using Gradient Descent.
* Visualize the final fitted regression line.

## 🛠️ Technologies Used

* Python
* NumPy
* Matplotlib
* Scikit-learn

## 🔄 Workflow

```text
Create Synthetic Data
        ↓
Visualize Data
        ↓
Standardize Features
        ↓
Split Data
        ↓
Initialize Parameters
        ↓
Generate Predictions
        ↓
Calculate Cost
        ↓
Apply Gradient Descent
        ↓
Update Parameters
        ↓
Repeat Until Convergence
        ↓
Evaluate the Model
```

## 📚 Main Concepts

### 1. Hypothesis Function

The hypothesis function generates predictions using the model parameters.

```python
def hypothesis(X, w0, w1):
    return w0 + w1 * X
```

Where:

* `w0` → Bias or intercept.
* `w1` → Weight or slope.
* `X` → Input feature.

The model predicts the output using the learned parameters.

### 2. Cost Function

The cost function measures how far the model's predictions are from the actual values.

A commonly used cost function is **Mean Squared Error (MSE)**.

A lower cost means the model's predictions are closer to the actual values.

### 3. Gradient Descent

Gradient Descent is an optimization algorithm used to minimize the cost function.

The algorithm repeatedly:

1. Calculates the model's error.
2. Calculates the gradients.
3. Updates the model parameters.
4. Repeats the process until the cost becomes smaller.

The learning rate controls the size of each update.

```text
Small Learning Rate → Slow Learning
Large Learning Rate → Possible Overshooting
```

### 4. Learning Rate

The learning rate determines how large each parameter update is.

A suitable learning rate helps the model converge efficiently toward the minimum cost.

### 5. Standardization

Standardization transforms features so that they have:

* Mean close to `0`
* Standard deviation close to `1`

This can help Gradient Descent converge more efficiently.

## 📊 Visualization

The notebook visualizes:

* The original synthetic dataset.
* The initial hypothesis.
* The cost during training.
* The final regression line.
* The relationship between the input feature and target variable.

## 🧠 Why Add Random Noise?

Random noise is added to synthetic data to make it more realistic.

Real-world data rarely follows a perfectly straight line. Noise represents small variations and unexpected factors that can affect the target variable.

## 📂 Repository Structure

```text
Univariate Linear Regression and Gradient Descent/
│
├── Univariate Linear Regression and Gradient Descent.ipynb
└── README.md
```

## 🚀 Conclusion

This project provides a practical understanding of how **Univariate Linear Regression** works and how **Gradient Descent** can be used to optimize model parameters.

Implementing these concepts from scratch helps build a strong foundation for understanding more advanced machine learning algorithms and optimization techniques.

