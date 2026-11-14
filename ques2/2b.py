import nltk
from nltk.corpus import stopwords

# Download stopwords dataset (run once)
nltk.download('stopwords')

def generate(text, n=2):
    # 1. Convert to lowercase, split by space, and remove stopwords in one line
    words = [word for word in text.lower().split() if word not in set(stopwords.words('english'))]
    
    # 2. The Pythonic N-Gram magic
    temp = zip(*[words[i:] for i in range(n)])

    # 3. Join the tuples back into strings (Fixed 'from' to 'for')
    ans = [' '.join(ngram_tuple) for ngram_tuple in temp]

    return ans

result = generate("The sun rises in the east and the sun sets in the west", 2)

print("N-grams:", result)