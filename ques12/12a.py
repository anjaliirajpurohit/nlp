import pandas as pd
import matplotlib.pyplot as plt
import string
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer

# Download stopwords (Run once per machine)
nltk.download('stopwords')

# 1. Read dataset
# encoding="latin-1" is required for this specific Kaggle spam.csv dataset
messages = pd.read_csv("spam.csv", encoding="latin-1")

# Drop unnecessary junk columns created by the CSV
messages = messages.drop(labels=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
messages.columns = ["label", "message"]

# Wrap EDA commands in print() so they show up in the terminal!
print("Dataset Info:")
print(messages.info())
print("\nDataset Head:")
print(messages.head())

# 2. Text preprocessing function
def text_preprocessing(mess):
    # Remove punctuation
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = "".join(nopunc).lower()

    # Remove stopwords and numbers
    nostop = [
        word for word in nopunc.split()
        if word not in stopwords.words('english') and word.isalpha()
    ]
    return nostop

# 3. Separate spam and ham messages for WordClouds
spam_messages = messages[messages["label"] == "spam"]["message"]
ham_messages = messages[messages["label"] == "ham"]["message"]

print(f"\nNo of spam messages: {len(spam_messages)}")
print(f"No of ham messages: {len(ham_messages)}")

# Extract words for Spam
spam_words = []
for message in spam_messages:
    spam_words.extend(text_preprocessing(message))

# 4. Generate Spam Word Cloud
spam_wordcloud = WordCloud(width=600, height=400).generate(" ".join(spam_words))
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(spam_wordcloud)
plt.axis("off")
plt.title("Spam Words")
plt.show()

print("\nTop 10 spam words are:")
print(pd.Series(spam_words).value_counts().head(10))

# 5. Apply preprocessing to the whole dataset
print("\nCleaning entire dataset...")
# Apply the function, then join the resulting list of words back into a clean string
messages["clean_message"] = messages["message"].apply(text_preprocessing)
messages["clean_message"] = messages["clean_message"].apply(lambda x: " ".join(x))

# 6. Bag of Words (CountVectorizer)
vectorizer = CountVectorizer()
messages_bow = vectorizer.fit_transform(messages['clean_message'])

print("\n--- Bag of Words Info ---")
print("Total number of unique vocabulary words:", len(vectorizer.vocabulary_))
print("Shape of sparse matrix:", messages_bow.shape)
print("Amount of non-zero occurrences:", messages_bow.nnz)