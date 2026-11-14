import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# 1. Download required datasets (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Sample text with lots of punctuation and repeated words
text = """
NLP is amazing! NLP is fun. We love studying NLP, 
because studying data is the future of data. 
Data, data, data... it's everywhere!
"""

# Step 1: Tokenize and convert to lowercase
# We lowercase everything so "Data" and "data" are counted as the same word
words = nltk.word_tokenize(text.lower())

# Step 2: Get the list of English stop words
stop_words = set(stopwords.words('english'))

# Step 3: Filter out stop words AND punctuation
# .isalpha() checks if the string is made of only alphabet letters (no punctuation or numbers)
clean_words = [word for word in words if word not in stop_words and word.isalpha()]

# Step 4: Count the frequencies 
freq = FreqDist(clean_words)

# Step 5: Print the top 5 most common words in the console
print("Most common words:", freq.most_common(5))

# Step 6: Plot the graph for the top 5 words
# Note: This will pop open a graph window on a local lab computer!
freq.plot(5, title="Top 5 Most Frequent Words")
plt.show()