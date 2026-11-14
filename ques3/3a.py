import nltk 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer

# Download required datasets for lab computers
nltk.download('punkt')
nltk.download('wordnet')

def analysis(sent):
    words = word_tokenize(sent)
    
    # 1. Porter Stemmer (The Classic)
    port = PorterStemmer()
    port_stem = [port.stem(word) for word in words]

    # 2. Lancaster Stemmer (The Aggressive one)
    lan = [LancasterStemmer().stem(word) for word in words]

    # 3. Snowball Stemmer (Fixed: Added 'english')
    snow = [SnowballStemmer('english').stem(word) for word in words]

    # 4. WordNet Lemmatizer (The Smart one)
    lemma = [WordNetLemmatizer().lemmatize(word) for word in words]

    print("Original:", sent)
    print("Porter:  ", port_stem)
    print("Lancast: ", lan)
    print("Snowball:", snow)
    print("Lemma:   ", lemma)

# Added a space after the period so word_tokenize splits it cleanly
sent = "Hey there what are you doing. they are hanging on the trees"
analysis(sent)