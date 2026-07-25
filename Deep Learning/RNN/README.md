# Recurrent Neural Networks (RNNs)

This folder contains learning materials and implementations of **Recurrent Neural Networks (RNNs)**, a type of Deep Learning model designed to work with sequential data.

## 📌 What is an RNN?

A **Recurrent Neural Network (RNN)** is a type of neural network that processes sequential data by using information from previous steps to help make predictions.

Unlike traditional neural networks, RNNs have a form of **memory** that allows them to use information from earlier parts of a sequence.

### Example

```text
Previous Words
      ↓
     RNN
      ↓
Next Word Prediction
```

For example:

```text
Input:
I am learning

Prediction:
Python
```

## 🧠 How RNNs Work

An RNN processes data one step at a time while passing information from the previous step to the next step.

```text
x₁ → RNN → h₁
           ↓
x₂ → RNN → h₂
           ↓
x₃ → RNN → h₃
           ↓
        Output
```

The hidden state carries information from previous time steps.

## 📚 Topics Covered

* Introduction to Recurrent Neural Networks
* Sequential Data
* Hidden States
* Recurrent Connections
* Time Steps
* Forward Propagation
* Backpropagation Through Time (BPTT)
* Vanishing Gradient Problem
* Long-Term Dependencies
* RNN Training
* Model Prediction
* Model Evaluation

## 🎯 Learning Objectives

By studying RNNs, you will learn:

* What Recurrent Neural Networks are
* How RNNs process sequential data
* How hidden states store information
* How information flows through time steps
* How RNNs make predictions
* What the Vanishing Gradient Problem is
* Why advanced models such as LSTM and GRU are used

## 🛠️ Libraries Used

* Python
* NumPy
* Pandas
* Matplotlib
* TensorFlow / Keras
* Scikit-learn

## 📂 Folder Structure

```text
RNN/
│
├── Recurrent Neural Networks.ipynb
└── README.md
```

## 📌 Applications of RNNs

RNNs are widely used in:

* Time Series Forecasting
* Text Generation
* Sentiment Analysis
* Speech Recognition
* Language Modeling
* Machine Translation
* Sequence Prediction
* Video Analysis

## 📌 Conclusion

Recurrent Neural Networks are designed to work with sequential data by using information from previous time steps. They form the foundation for advanced sequence models such as **LSTM** and **GRU**, which are designed to handle long-term dependencies more effectively.

