
# =====================================
# TWITTER SENTIMENT ANALYSIS
# =====================================

# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from textblob import TextBlob
from wordcloud import WordCloud

# 2. Download NLTK Resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# 3. Load Dataset
df = pd.read_csv("data.csv")

print("\nDataset Preview:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# 4. Select Required Columns
text_df = df[['user_name', 'text']].copy()
text_df.dropna(subset=['text'], inplace=True)

# 5. Text Preprocessing
def clean_text(text):

    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#', '', text)

    # Remove punctuation and numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenization
    words = word_tokenize(text)

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    return " ".join(words)


text_df['text'] = text_df['text'].apply(clean_text)

# Remove Duplicate Tweets
text_df.drop_duplicates(subset='text', inplace=True)

print("\nCleaned Tweets:")
print(text_df.head())

# 6. Stemming
stemmer = PorterStemmer()

def stemming(text):

    words = text.split()
    words = [stemmer.stem(word) for word in words]

    return " ".join(words)


text_df['text'] = text_df['text'].apply(stemming)

print("\nAfter Stemming:")
print(text_df['text'].head())

# 7. Sentiment Polarity
def polarity(text):
    return TextBlob(text).sentiment.polarity


text_df['polarity'] = text_df['text'].apply(polarity)

# 8. Sentiment Classification
def sentiment(p):

    if p > 0:
        return 'Positive'

    elif p < 0:
        return 'Negative'

    else:
        return 'Neutral'


text_df['sentiment'] = text_df['polarity'].apply(sentiment)

print("\nSentiment Analysis Results:")
print(text_df[['text', 'polarity', 'sentiment']].head(10))

# 9. Sentiment Distribution
counts = text_df['sentiment'].value_counts()

print("\nSentiment Distribution:")
print(counts)

# 10. Bar Graph
plt.figure(figsize=(8, 5))

sns.countplot(data=text_df, x='sentiment', hue='sentiment',
              palette='viridis', legend=False)

plt.title("Twitter Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")

plt.tight_layout()

plt.savefig("bar_chart.png", dpi=300)
plt.show()

# 11. Pie Chart
plt.figure(figsize=(7, 7))

plt.pie(
    counts,
    labels=counts.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Sentiment Percentage Distribution")

plt.tight_layout()

plt.savefig("pie_chart.png", dpi=300)
plt.show()
# 12. WordCloud
all_words = " ".join(text_df['text'])

if all_words.strip():

    wordcloud = WordCloud(
        width=1000,
        height=500,
        background_color='white',
        max_words=200
    ).generate(all_words)

    plt.figure(figsize=(12, 6))

    plt.imshow(wordcloud, interpolation='bilinear')

    plt.axis('off')

    plt.title("Most Frequently Used Words")

    plt.tight_layout()
    plt.savefig("wordcloud.png")
    plt.show()

else:
    print("No words available for WordCloud.")

# 13. Save Results
text_df.to_csv("sentiment_results.csv", index=False)

print("\nSentiment Analysis Completed Successfully!")
print("Results saved in sentiment_results.csv")
