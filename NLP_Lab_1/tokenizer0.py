import re, sys

for line in sys.stdin:
    for token in re.split(r"\s+", line.strip()):
        print(token)
