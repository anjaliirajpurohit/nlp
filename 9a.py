non_terminals = ['NP', 'Noun', 'Det', 'AP', 'Adv']

# Converted strictly to Chomsky Normal Form (CNF)
R = {
    "NP": [["Det", "Noun"]], 
    
    # Added ["Noun", "Noun"] so "orange" and "man" can combine
    "Noun": [["AP", "Noun"], ["Noun", "Noun"], ["book"], ["orange"], ["man"]], 
    
    "Det": [["a"], ["the"]],
    
    "AP": [["Adv", "AP"], ["tall"]], 
    
    "Adv": [["very"]]
}

def cykParse(w):
    n = len(w)
    # Initialize the n x n matrix with empty sets
    T = [[set() for j in range(n)] for i in range(n)]

    for j in range(0, n):
        # Step 1: Fill the diagonal with Terminal rules
        for lhs, rule in R.items():
            for rhs in rule:
                if len(rhs) == 1 and rhs[0] == w[j]:
                    T[j][j].add(lhs)

        # Step 2: Fill the rest of the matrix with Non-Terminal rules
        for i in range(j, -1, -1):
            for k in range(i, j):
                for lhs, rule in R.items():
                    for rhs in rule:
                        # Only check strict length-2 CNF rules
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k+1][j]:
                            T[i][j].add(lhs)

    # Optional: Print matrix in a cleaner way for debugging
    # for row in T:
    #     print(row)

    # If 'NP' is in the top-right corner of the matrix, it's a valid sentence
    if "NP" in T[0][n-1]:
        print("True")
    else:
        print("False")

# Test the program
w = "a very tall orange man".split()
cykParse(w)