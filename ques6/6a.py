import nltk
from textblob import TextBlob  # FIX 1: Imported TextBlob

# Download necessary datasets (run once per machine)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sent = "Ravi is a bad leader. He misguides the team"

# Tokenize the sentence into words
words = nltk.word_tokenize(sent)

# Assign POS tags to each word
sentpos = nltk.pos_tag(words)

# FIX 2: Changed p[i] to p[1] to check the tag
n = " ".join([p[0] for p in sentpos if p[1] in ['NNP', 'NN']])

# FIX 3: Changed JJJ to JJS
a = " ".join([p[0] for p in sentpos if p[1] in ['JJ', 'JJR', 'JJS']])

print("Nouns:", n)
print("Adj:", a)

# Calculate sentiment using TextBlob
print("Sentiment score:", TextBlob(a).sentiment)