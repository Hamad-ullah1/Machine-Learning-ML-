# Next Word Prediction Using LSTM

This folder contains a deep learning implementation of **Next Word Prediction using Long Short-Term Memory (LSTM)** networks.

## 📌 What is Next Word Prediction?

**Next Word Prediction** is the task of predicting the most likely word that comes next in a sequence of text.

### Example

```text
Input:
I am learning

Prediction:
Python
```

The model learns patterns from existing text and predicts the next word based on the previous words.

## 🧠 Why Use LSTM?

LSTM networks are useful for next word prediction because they can remember important information from previous words in a sequence.

For example:

```text
The cat sat on the ___
```

The model may predict:

```text
mat
```

The prediction is based on patterns learned from the training data.

## 🔄 How It Works

```text
Text Dataset
     ↓
Tokenization
     ↓
Create Input Sequences
     ↓
Padding
     ↓
LSTM Model
     ↓
Training
     ↓
Predict Next Word
```

## 📚 Topics Covered

* Natural Language Processing (NLP)
* Text Preprocessing
* Tokenization
* Vocabulary Creation
* Input Sequences
* Sequence Padding
* LSTM Architecture
* Embedding Layer
* Model Training
* Next Word Prediction
* Text Generation

## 🎯 Learning Objectives

By studying this project, you will learn:

* How text data is prepared for deep learning
* How tokenization works
* How input sequences are created
* How padding makes sequences equal in length
* How LSTM learns patterns from text
* How to train an LSTM model
* How to predict the next word in a sentence
* How to generate text using a trained model

## 🛠️ Libraries Used

* Python
* NumPy
* Pandas
* TensorFlow / Keras
* Matplotlib

## 📂 Folder Structure

```text
Next Word Prediction Using LSTM/
│
├── Next Word Prediction Using LSTM.ipynb
└── README.md
```

## 📌 Example

```text
Input:
Machine learning is

Predicted next word:
powerful
```

The model predicts the next word based on the patterns it learned from the training text.

## 📌 Applications

Next Word Prediction is used in:

* Text Autocomplete
* Chatbots
* Search Engines
* Mobile Keyboard Suggestions
* Text Generation
* Natural Language Processing Applications

## 📌 Conclusion

Next Word Prediction using LSTM demonstrates how deep learning models can learn patterns in sequential text data. By using tokenization, sequence preparation, embeddings, and LSTM layers, the model can predict the most likely next word based on previous words.

