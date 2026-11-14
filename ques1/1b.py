import nltk 
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# 1. Download necessary NLTK datasets (run this once per machine)
nltk.download('punkt')
nltk.download('stopwords')

example = "'hi there we are studying. Studying is whatver. i sometimes like studying and sometime i do not'"

# 2. Tokenization: Break the paragraph into sentences
sent = nltk.sent_tokenize(example)
print("Sentences:", sent)

# Initialize the stemmer properly with parentheses
stemmer = PorterStemmer()

# Load the stopwords into a set once (faster than doing it inside the loop)
stop_words = set(stopwords.words('english'))

for i in range(len(sent)):
    # Tokenization: Break the sentence into words
    words = nltk.word_tokenize(sent[i])
    
    # 3 & 4. Stop Word Removal and Stemming
    # We also use word.lower() to ensure words like "Studying" aren't missed by the lowercase stopword list
    processed_words = [stemmer.stem(word.lower()) for word in words if word.lower() not in stop_words]

    # Rejoin the words with a space
    sent[i] = ' '.join(processed_words)
    
    print(f"Processed words for sentence {i+1}:", processed_words)
  