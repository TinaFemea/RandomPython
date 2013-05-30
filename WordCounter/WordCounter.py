__author__ = 'tina'

import os.path


def getFileName():
    """Prompts the user for a file name.  Verifies existence."""
    fileName = raw_input("enter a file name: ")

    while not os.path.exists(fileName):
        fileName = raw_input("enter a file name (that actually exists): ")

    return fileName


def processWordList(listOfWords, wordDict):
    """Adds one to the counter in wordDict for every word in listOfWords"""
    for word in listOfWords:
        lowercaseTrimmedWord = trimPunctuation(word.lower())
        if len(lowercaseTrimmedWord) == 0:
            continue
        if lowercaseTrimmedWord in wordDict:
            wordDict[lowercaseTrimmedWord] += 1
        else:
            wordDict[lowercaseTrimmedWord] = 1


def prettyPrintWordList(wordDict):
    """ Prints the dictionary, sorted, in a human-readable way"""
    sortedKeys = wordDict.keys()
    sortedKeys.sort()
    for currentWord in sortedKeys:
        print "%s: %s" % (currentWord, wordDict[currentWord])


def trimPunctuation(word):
    """Trims off anything from the beginning or end that isn't a letter or digit """
    firstRealCharacter = -1
    lastRealCharacter = -1
    wordLength = len(word)
    for i in range(wordLength):
        thisLetter = word[i]
        if thisLetter.isdigit() or thisLetter.isalpha():
            firstRealCharacter = i
            break

    if firstRealCharacter == -1:
        return ""

    for i in range(wordLength - 1, -1, -1):
        thisLetter = word[i]
        if thisLetter.isdigit() or thisLetter.isalpha():
            lastRealCharacter = i
            break

    return word[firstRealCharacter:lastRealCharacter + 1]



fileName = getFileName()
f = open(fileName, 'r')

wordDict = {}

currentLine = f.readline()
while currentLine != '':
    listOfWords = str.split(currentLine)
    processWordList(listOfWords, wordDict)
    currentLine = f.readline()

prettyPrintWordList(wordDict)

"""  Test cases
print trimPunctuation(".")
print trimPunctuation("a.")
print trimPunctuation("abcd")

print trimPunctuation("abcd,")
print trimPunctuation("abcd")
print trimPunctuation("--abcd")
print trimPunctuation("abcd---")

print trimPunctuation("--abcd---")
print trimPunctuation("--ab'cd---")
"""