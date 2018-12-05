from nltk import word_tokenize
from nltk import CFG
from nltk import ChartParser

def read_grammar(grammarfile):
    gf = open(grammarfile)
    return CFG.fromstring(gf.read())

def print_trees(trees):
    for t in trees:
        print(t)

def parse_sentences(grammar):
    parser = ChartParser(grammar)
    sent = input("Parse a sentence (Q to quit): ")
    while sent != "Q":
        tokens = word_tokenize(sent)
        trees = parser.parse(tokens)
        print_trees(trees)
        sent = input("Parse a sentence (Q to quit): ")
