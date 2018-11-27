import sys

def noun_lemma(word):
    word = remove_s(word)
    return word.lower()

def verb_lemma(word):
    word = aux_lemma(word)
    word = remove_s(word)
    if word.endswith("ed") or word.endswith("en"):
        return fix_ending(word[:-2])
    elif word.endswith("ing"):
        return fix_ending(word[:-3])
    else:
        return verb_irregular(word) 

def verb_irregular(word):
    irregular_dict = {
        "did": "do",
        "done": "do",
        "got": "get",
        "heard": "hear",
        "left": "leave",
        "gave": "give",
        "lost": "lose",
        "sent": "send",
        "saw": "see",
        "came": "come"
    }
    if word.lower() in irregular_dict:
        return irregular_dict[word.lower()]
    else:
        return word.lower()

def remove_s(word):
    if word.endswith("es"):
        if word[-3] in "szx" \
            or word[-4:2] == "ch" or word[-4:2] == "sh":
            return word[:-2].lower()
        elif word[-3] == "v":
            return word[:-3] + "f"
        else:
            return fix_ending(word[:-2])
    elif word.endswith("s") and word != "s" and word[-2] != "s":
        return word[:-1].lower()
    else:
        return word.lower()

def fix_ending(word):
    if word.endswith("i") and word != "i":
        return word[:-1].lower() + "y"
    else:
        return word.lower()

def aux_lemma(word):
    group_be = ["am", "is", "are", "was", "were", "been", "being", "\'s", "\'m", "\'re"]
    group_have = ["has", "had", "\'ve"]
    group_would = ["\'d"]
    if word.lower() in group_be:
        return "be"
    elif word.lower() in group_have:
        return "have"
    elif word.lower in group_would:
        return "would"
    else:
        return word.lower()

def adj_lemma(word):
    if word.endswith("er"):
        return word[:-2].lower()
    elif word.endswith("est"):
        return word[:-3].lower()
    else:
        return word.lower()

def pron_lemma(word):
    group_i = ["i", "me", "mine"]
    group_he = ["he", "him", "his"]
    group_she = ["she", "her", "hers"]
    group_we = ["we", "ours", "our"]
    group_you = ["you", "yours", "your"]
    group_they = ["they", "their", "them", "theirs"]

    if word.lower() in group_i:
        return "I"
    elif word.lower() in group_you:
        return "you"
    elif word.lower() in group_he:
        return "he"
    elif word.lower() in group_she:
        return "she"
    elif word.lower() in group_we:
        return "we"
    elif word.lower() in group_they:
        return "they"
    else:
        return word.lower()

def det_lemma(word):
    if word.lower() == "an":
        return "a"
    else:
        return word.lower()

def part_lemma(word):
    if word == "n\'t":
        return "not"
    else:
        return word.lower()

for line in sys.stdin:
    if line.strip():
        (word, tag) = line.strip().split("\t")
        lemma = word
        if tag == "NOUN":
            lemma = noun_lemma(word)
        elif tag == "VERB":
            lemma = verb_lemma(word)
        elif tag == "ADJ":
            lemma = adj_lemma(word)
        elif tag == "AUX":
            lemma = aux_lemma(word)
        elif tag == "PRON":
            lemma = pron_lemma(word)
        elif tag == "DET":
            lemma = det_lemma(word)
        elif tag == "PART":
            lemma = part_lemma(word)
        elif tag in ["ADP", "ADV", "SCONJ", "CONJ"]:
            lemma = lemma.lower()
        else:
            lemma = word
        print("{0}\t{1}\t{2}".format(word, tag, lemma))
    else:
        print()
