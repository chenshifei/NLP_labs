import re, sys

for line in sys.stdin:
    regex = re.compile(r'''
        ((?<=[.]) (?=[A-Z])|
        \d+\.\d+|
        n\'t|
        \'[sd]|
        (\w+-)+\w+|
        (\w+\.)+|
        \'\'?|
        [,;:.!?\"%$&]|
        --|
        ``|
        \w+)
    ''', re.VERBOSE)
    for token in re.findall(regex, line.strip()):
        if token[0].isspace():
            print(token[0])
        else:
            print(token[0])
