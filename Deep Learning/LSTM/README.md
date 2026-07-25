# Long Short-Term Memory (LSTM)

This folder contains learning materials and implementations of **Long Short-Term Memory (LSTM)** networks, a type of Recurrent Neural Network (RNN) designed to learn long-term dependencies in sequential data.

## 📌 What is LSTM?

**Long Short-Term Memory (LSTM)** is a type of **Recurrent Neural Network (RNN)** that is designed to remember important information for a long period of time and forget unnecessary information.

LSTMs are especially useful for **sequence-based data**.

### Example

```text id="m2y7v8"
Previous Information
        ↓
      LSTM
        ↓
Current Prediction
```

## 🧠 Why LSTM?

Traditional RNNs can have difficulty remembering information from far back in a sequence because of the **Vanishing Gradient Problem**.

LSTM networks solve this problem using a special memory structure and gates.

## 🚪 LSTM Gates

An LSTM uses three main gates:

### 1. Forget Gate

Decides which information should be removed from the cell state.

### 2. Input Gate

Decides which new information should be stored.

### 3. Output Gate

Decides which information should be used as the output.

```text id="v2uj8q"
Input
  ↓
Forget Gate
  ↓
Input Gate
  ↓
Cell State
  ↓
Output Gate
  ↓
Output
```

## 📚 Topics Covered

* Introduction to LSTM
* Recurrent Neural Networks
* Sequential Data
* Long-Term Dependencies
* Vanishing Gradient Problem
* LSTM Architecture
* Cell State
* Forget Gate
* Input Gate
* Output Gate
* Sequence Processing
* Model Training
* Model Evaluation

## 🎯 Learning Objectives

By studying LSTM, you will learn:

* What LSTM networks are
* Why LSTM is used for sequential data
* How LSTM remembers important information
* How LSTM forgets unnecessary information
* How the three gates work
* How LSTM solves the vanishing gradient problem
* How to train and evaluate an LSTM model

## 🛠️ Libraries Used

* Python
* NumPy
* Pandas
* Matplotlib
* TensorFlow / Keras
* Scikit-learn

## 📂 Folder Structure

```text id="d0j6z5"
LSTM/
│
├── LSTM.ipynb
└── README.md
```

## 📌 Applications of LSTM

LSTM networks are widely used in:

* Time Series Forecasting
* Text Generation
* Sentiment Analysis
* Speech Recognition
* Machine Translation
* Next Word Prediction
* Video Analysis

## 📌 Conclusion

LSTM is a powerful type of Recurrent Neural Network that can learn long-term dependencies in sequential data. Its memory cell and gates allow it to remember important information and forget unnecessary information, making it useful for many sequence-based tasks.

