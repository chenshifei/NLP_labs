import re, sys

for line in sys.stdin:
    regex = re.compile(r'''
        (\d+\.\d+|
        n\'t|
        \'[sd]|
        (\w+-)+\w+|
        [A-Z]\w*\.(\w+\.)*|
        \'\'?|
        [,;:.!?\"%$&]|
        --|
        \w+(?=n\'t)|
        \w+)
    ''', re.VERBOSE)
    for token in re.findall(regex, line.strip()):
        print(token[0])
