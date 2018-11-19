import sys
import nltk
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import re

text = []
for line in sys.stdin:
    text.append(line.strip())

text = ' '.join(text)
sentences = sent_tokenize(text)
for sen in sentences:
    tokens = word_tokenize(sen)
    for tok in tokens:
        print(tok)
    print()

