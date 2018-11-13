import re, sys

for line in sys.stdin:
    regex = re.compile(r'''
        ((?<=\.)\s(?=[A-Z])|
        \d+\.\d+|
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
    for token in re.findall(regex, line):
        if token[0].isspace():
            print('')
        else:
            print(token[0])
