import re
import string
import cProfile
import sys
global integerK


def setToDictionary(diction, textfile, invalidChars):
    integerK = 100
    file = open(textfile, 'r', encoding='utf-8')
    for line in file:
        kString = ""
        for c in line:
            if c.isdigit():
                kString += c
            else:
                integerK = kString
                break
        break
    with file as f:
        for line in f:
            for word in line.split():
                if word.isalpha():
                    word = word.lower()
                    if word in dictionary:
                        diction[word] += 1
                    else:
                        diction[word] = 1
    return diction, integerK


dictionary = {}
textfile = sys.argv[1]
invalidChars = set(string.punctuation)
dictionary, integerK = setToDictionary(dictionary, textfile, invalidChars)
sortedDictionary = sorted([i for i in dictionary])
dictionary2 = {key: dictionary[key] for key in sortedDictionary}
sortedDictionary2 = sorted(dictionary2, key=dictionary2.get, reverse=True)
for i in range(0, int(integerK)):
    print(sortedDictionary2[i], dictionary2[sortedDictionary2[i]])
