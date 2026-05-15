# SMS Spam Classifier

## Overview

SMS Spam Classifier is a Machine Learning web application that classifies SMS messages as either Spam or Not Spam using Natural Language Processing (NLP) techniques and a trained Multinomial Naive Bayes model.

The application is built with Python, Scikit-learn, NLTK, and Streamlit, providing a lightweight and interactive interface for real-time spam detection.

---

## Live Application

https://sms-spam-classifier-xvv7cpgwyb4gqccsoaqbux.streamlit.app/

---

## Features

- Real-time SMS spam detection
- Text preprocessing and normalization
- Tokenization and stopword removal
- Stemming using Porter Stemmer
- TF-IDF vectorization
- Machine Learning based prediction
- Interactive Streamlit interface
- Lightweight deployment on Streamlit Cloud

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend Framework | Streamlit |
| Machine Learning | Scikit-learn |
| NLP Processing | NLTK |
| Data Processing | Pandas, NumPy |
| Model | Multinomial Naive Bayes |
| Vectorization | TF-IDF Vectorizer |

---

## Project Structure

```bash
sms-spam-classifier/
│
├── app.py
├── train_model.py
├── spam.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── runtime.txt
└── README.md
```

### File Descriptions

| File | Description |
|---|---|
| `app.py` | Main Streamlit application |
| `train_model.py` | Script used for model training |
| `spam.csv` | SMS spam dataset |
| `model.pkl` | Trained MultinomialNB model |
| `vectorizer.pkl` | Saved TF-IDF vectorizer |
| `requirements.txt` | Python dependencies |
| `runtime.txt` | Python runtime version |
| `README.md` | Project documentation |

---

## Installation and Setup

### Clone Repository

```bash
git clone https://github.com/vishyy27/sms-spam-classifier.git
cd sms-spam-classifier
```

---

### Create Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Download Required NLTK Resources

Run the following commands once:

```python
import nltk

nltk.download('punkt')
nltk.download('stopwords')
```

---

### Run Application

```bash
streamlit run app.py
```

---

## Machine Learning Pipeline

The spam classification workflow consists of the following stages:

1. Text Cleaning and Lowercasing
2. Tokenization
3. Removal of Special Characters
4. Stopword Removal
5. Word Stemming
6. TF-IDF Feature Extraction
7. Prediction using Multinomial Naive Bayes

---

## Dataset Information

The dataset used for training contains labeled SMS messages categorized into:

- Spam
- Ham (Non-Spam)

The dataset is stored in `spam.csv`.

---

## Model Details

| Component | Value |
|---|---|
| Algorithm | Multinomial Naive Bayes |
| Feature Extraction | TF-IDF Vectorization |
| NLP Library | NLTK |
| Model Serialization | Pickle |

---

## Deployment

The application is deployed using Streamlit Cloud.

### Deployment Platform

- Streamlit Cloud

### Deployment Files

| File | Purpose |
|---|---|
| `requirements.txt` | Dependency installation |
| `runtime.txt` | Python runtime specification |

---

## Future Improvements

- Improve model accuracy using advanced NLP techniques
- Add confidence score visualization
- Add support for multiple languages
- Integrate deep learning based classifiers
- Add message history and analytics dashboard

---

## Contributing

Contributions are welcome.

### Steps to Contribute

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---

## Author

Vishwas Desai

GitHub: https://github.com/vishyy27
