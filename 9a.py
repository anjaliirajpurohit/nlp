# 1. Chomsky Normal Form (CNF) Grammar
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "Nominal"], ["Det", "Noun"]],
    "Nominal": [["AP", "Noun"]],
    "VP": [["Verb", "NP"]],
    "AP": [["tall"]],
    "Det": [["the"], ["a"]],
    "Noun": [["student"], ["book"]],
    "Verb": [["reads"]]
}

def cyk_parser(sentence):
    n = len(sentence)
    # Create an n x n table filled with empty lists
    table = [[[] for _ in range(n)] for _ in range(n)]
    
    # Step 1: Fill the diagonal cells (Single words)
    for i, word in enumerate(sentence):
        for parent, rules in grammar.items():
            for rule in rules:
                if len(rule) == 1 and rule[0] == word:
                    table[i][i].append(parent)
                    
    # Step 2: Fill the rest of the table (Combining spans)
    for length in range(2, n + 1):          # Span length (2 to n)
        for start in range(n - length + 1): # Start position
            end = start + length - 1        # End position
            
            for split in range(start, end): # Split point
                left = table[start][split]
                right = table[split + 1][end]
                
                for parent, rules in grammar.items():
                    for rule in rules:
                        # Check binary rules (A -> B C)
                        if len(rule) == 2 and rule[0] in left and rule[1] in right:
                            if parent not in table[start][end]:
                                table[start][end].append(parent)

    # Step 3: Check top-right corner for Start symbol 'S'
    return "S" in table[0][n - 1]

# Test the program
sentence = "the tall student reads a book".split()
print("Is the sentence valid?", cyk_parser(sentence))