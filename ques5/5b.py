import nltk

# 1. Download necessary datasets (run once per machine)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def process_and_draw(text):
    print("Original Text:", text, "\n")

    # Step 1: Tokenize (Break sentence into words)
    words = nltk.word_tokenize(text)
    
    # Step 2: POS Tagging (Assign a Part-of-Speech label to each word)
    # This creates a list of pairs like ('dog', 'NN')
    tagged_words = nltk.pos_tag(words)
    print("Part-of-Speech Tags:")
    print(tagged_words, "\n")

    # Step 3: Parsing (Build a tree structure from the tags)
    # We create a simple grammar rule to group Nouns and Adjectives
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    parser = nltk.RegexpParser(grammar)
    
    # Parse the tagged words into a Tree structure
    parsed_tree = parser.parse(tagged_words)
    
    # Step 4: Display the parsed result
    print("Parsed Tree Structure:")
    print(parsed_tree)

    # Note for Lab: If you are running this on the college's local Python IDLE,
    # uncomment the line below to pop open a visual graphical drawing of the tree!
    # parsed_tree.draw()

# Test the function
sample_text = "A smart student writes clean Python code."
process_and_draw(sample_text)