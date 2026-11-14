def simple_viterbi():
    # 1. Our HMM Dictionary Data
    pos_tags = ['ADJ', 'V', 'N']

    # Likelihood of starting a sentence
    initial_p = {'ADJ': 0.4, 'V': 0.4, 'N': 0.2}

    # Likelihood of Tag B following Tag A
    trans_p = {
        'ADJ': {'ADJ': 0.1, 'V': 0.1, 'N': 0.8},
        'V':   {'ADJ': 0.2, 'V': 0.1, 'N': 0.7},
        'N':   {'ADJ': 0.1, 'V': 0.6, 'N': 0.3}
    }

    # Likelihood of a Tag producing a specific Word
    emit_p = {
        'ADJ': {'free': 0.8, 'workers': 0.0},
        'V':   {'free': 0.5, 'workers': 0.0},
        'N':   {'free': 0.0, 'workers': 0.9}
    }

    # ==========================================
    # STEP 1: Calculate scores for word 1 ("free")
    # Formula: Initial Probability * Emission Probability
    # ==========================================
    step1_scores = {}
    
    for tag in pos_tags:
        score = initial_p[tag] * emit_p[tag]['free']
        step1_scores[tag] = score
        
    print("Scores after 'free':", step1_scores)

    # ==========================================
    # STEP 2: Calculate scores for word 2 ("workers")
    # Formula: Prev Score * Transition * Emission
    # ==========================================
    step2_scores = {}
    best_previous_tag = {} # To remember our path

    for current_tag in pos_tags:
        highest_score = 0
        best_path = ""

        # Check all possible previous tags to find the highest pathway
        for prev_tag in pos_tags:
            score = step1_scores[prev_tag] * trans_p[prev_tag][current_tag] * emit_p[current_tag]['workers']
            
            # If this path is the best one we've seen so far, save it!
            if score > highest_score:
                highest_score = score
                best_path = prev_tag

        step2_scores[current_tag] = highest_score
        best_previous_tag[current_tag] = best_path

    print("Scores after 'workers':", step2_scores)

    # ==========================================
    # STEP 3: Find the winner and backtrack
    # ==========================================
    
    # 1. Find which tag won at the very end
    final_tag = 'N' # We can see N will win because "workers" is a noun, but let's be safe
    highest_final = 0
    for tag in pos_tags:
        if step2_scores[tag] > highest_final:
            highest_final = step2_scores[tag]
            final_tag = tag

    # 2. Look at our saved path to see what came before the final tag
    first_tag = best_previous_tag[final_tag]

    print("\n--- FINAL RESULT ---")
    print(f"Sentence: ['free', 'workers']")
    print(f"Winning POS Tags: ['{first_tag}', '{final_tag}']")

# Run the program
simple_viterbi()