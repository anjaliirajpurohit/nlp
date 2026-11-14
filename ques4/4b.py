import nltk

# 1. Download required NLTK datasets (run this once per machine)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# 2. Our sample sentence
sentence = "The little yellow dog barked at the cat."

# 3. Tokenize: Break sentence into words
words = nltk.word_tokenize(sentence)

# 4. POS Tagging: Label each word (Noun, Verb, Adjective, etc.)
tagged_words = nltk.pos_tag(words)
print("Tagged Words:\n", tagged_words, "\n")

# 5. Define the Regex Pattern (The Grammar Rule)
# NP (Noun Phrase) Rule: 
# <DT>?  -> Optional Determiner (like "the", "a")
# <JJ>*  -> Zero or more Adjectives (like "little", "yellow")
# <NN>   -> Exactly one Noun (like "dog", "cat")
grammar = "NP: {<DT>?<JJ>*<NN>}"

# 6. Build the parser and extract the chunks
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(tagged_words)

# 7. Print the final chunked tree
print("Chunking Result:")
print(tree)

# Optional: If you run this on a local computer with a screen, 
# this command will pop up a cool visual diagram of your chunks!
tree.draw()