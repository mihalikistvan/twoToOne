def longest(a1, a2):
    tempList =  [letter for letter in a1] + [letter for letter in a2]
    return ''.join(sorted(set(tempList)))
