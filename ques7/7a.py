import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# 1. Download required NLTK datasets (Run this once per machine)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# 2. Helper function to translate POS tags
def get_wordnet_pos(treebank_tag):
    """
    NLTK's pos_tag() returns 'Penn Treebank' tags (like 'NN' or 'VBZ').
    But the WordNetLemmatizer only understands 'WordNet' tags (like 'n' or 'v').
    This function translates them so the lemmatizer knows what to do.
    """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ    # Adjective (JJ)
    elif treebank_tag.startswith('V'):
        return wordnet.VERB   # Verb (VB, VBG, etc.)
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN   # Noun (NN, NNP, etc.)
    elif treebank_tag.startswith('R'):
        return wordnet.ADV    # Adverb (RB)
    else:
        return wordnet.NOUN   # Default to Noun if it's something else

def morphological_analysis(text):
    print(f"Original Text: {text}\n")
    
    # Initialize the Lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Step 1: Tokenize
    words = word_tokenize(text)
    
    # Step 2: Tag Parts of Speech
    tagged_words = nltk.pos_tag(words)
    
    print(f"{'Original Word':<15} | {'POS Tag':<10} | {'Root Lemma'}")
    print("-" * 45)
    
    # Step 3: Loop through and Lemmatize based on POS
    for word, tag in tagged_words:
        # Translate the tag
        wn_tag = get_wordnet_pos(tag)
        
        # Lemmatize using BOTH the word and its specific POS tag
        lemma = lemmatizer.lemmatize(word.lower(), pos=wn_tag)
        
        print(f"{word:<15} | {tag:<10} | {lemma}")

# Test the program with a sentence full of different word forms
sample_text = "The running dogs are easily jumping over the highest fences."
morphological_analysis(sample_text)