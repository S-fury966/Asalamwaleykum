logical_flips = {

"always":"never",
"never":"always",
"secure":"insecure",
"safe":"unsafe",
"is":"is not",
"are":"are not"

}

def logical_flip(prompt):

    words = prompt.split()

    new_words = []

    for w in words:

        if w.lower() in logical_flips:

            new_words.append(logical_flips[w.lower()])

        else:

            new_words.append(w)

    return " ".join(new_words)