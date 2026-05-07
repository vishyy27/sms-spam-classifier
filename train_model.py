import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("spam.csv", encoding='latin-1')

# Keep required columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# Convert labels
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Features and labels
X = df['message']
y = df['label']

# Create vectorizer
tfidf = TfidfVectorizer()

# Transform text
X = tfidf.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save vectorizer
pickle.dump(tfidf, open('vectorizer.pkl', 'wb'))

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

