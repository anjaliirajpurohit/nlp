import nltk
from nltk.probability import FreqDist

# 1. Download required NLTK datasets (run once per machine)
nltk.download('punkt')

# Step 1: Create a collection of 3 documents
doc1 = "Natural language processing is a fascinating field of study."
doc2 = "Studying natural language processing helps us understand AI."
doc3 = "AI is a fascinating field, and natural language processing is the future!"

# Step 2: Combine all documents into one giant string for corpus-level analysis
# We convert it to lowercase so "Natural" and "natural" are treated the same
collection = doc1.lower() + " " + doc2.lower() + " " + doc3.lower()

# Step 3: Tokenize and clean the text (keep only words, drop punctuation)
words = nltk.word_tokenize(collection)
clean_words = [word for word in words if word.isalpha()]

# Step 4: Generate the bi-grams (pairs of consecutive words)
# nltk.bigrams() creates an iterator, so we wrap it in list() to see the pairs
bi_grams = list(nltk.bigrams(clean_words))

# Step 5: Calculate the frequencies using FreqDist
freq = FreqDist(bi_grams)

# Step 6: Find the total number of UNIQUE bi-grams
total_unique_bigrams = len(freq)
print(f"Total number of unique bi-grams: {total_unique_bigrams}\n")

# Step 7: Display the top 5 most common bi-grams
print("Top 5 most common bi-grams:")
for bigram, count in freq.most_common(5):
    print(f"{bigram}: {count} times")