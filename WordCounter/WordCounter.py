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

def invertDictionary(wordDict):
    """Takes a dictionary of word:count and returns it as a dictionary of count:list of words"""
    invertedDict = {}
    for currentWord in wordDict:
        wordCount = wordDict[currentWord]
        if not wordCount in invertedDict:
            invertedDict[wordCount] = []
        invertedDict[wordCount].append(currentWord)
    return invertedDict


def prettyPrintInvertedWordList(invertedList):
    """Pretty-prints a dictionary of count:list of words"""
    sortedKeys = invertedList.keys()
    sortedKeys.sort()
    for currentCount in sortedKeys:
        wordsForCount = invertedList[currentCount]
        wordsForCount.sort()
        print "%d:" % currentCount
        for thisWord in wordsForCount:
            print "    %s" % thisWord


def prettyPrintWordList(wordDict):
    """ Prints the dictionary of type word:count, sorted, in a human-readable way"""
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
invertedDictionary = invertDictionary(wordDict)
prettyPrintInvertedWordList(invertedDictionary)

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