pos_tags = ['ADJ','V','N']

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


first_score = {}

for tag in pos_tags:
    score = initial_p[tag]*emit_p[tag]['free']
    first_score[tag] = score

print("Scores after first tag",first_score)


second_score = {}
best_previous_path = {}

for curr in pos_tags:
    high = 0
    best = ""

    for prev_tag in pos_tags:
        score = first_score[prev_tag]*trans_p[prev_tag][curr]*emit_p[curr]['workers']

        if score>high:
            high = score
            best = prev_tag
    

    second_score[curr] =high
    best_previous_path[curr] = best

print("Scores after workers:",second_score)


final = "N"
highest = 0
for tag in pos_tags:
    if second_score[tag]>highest:
        highest = second_score[tag]
        final = tag

first_tag = best_previous_path[final]

print(f"{first_tag},{final}")