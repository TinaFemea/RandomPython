__author__ = 'tina'

def ReverseArray(listOfChars):
    """ Takes a list (not a string!) of characters and returns them as a string in reverse order."""
    listOfChars.reverse()
    return "".join(listOfChars)
    # above is functionally identical to this but not O(n^2)
    #for reversedChar in listOfChars:
    #    reversedString += reversedChar


def ReverseLine(inputLine):
    """ Takes a string and returns a new string, where only the letters inside words are reversed.
        Punctuation is preserved" """
    listOfChars = []
    reversedLine = ""
    for currentChar in inputLine:
        if currentChar.isalpha():   # if it's a letter, it's part of a word, add it to the list.
            listOfChars.append(currentChar)
        else:
        # it's not a letter.  Reverse all the letters we've seen so far, clear the list, then write out this character
            if len(listOfChars) > 0:
                reversedLine += ReverseArray(listOfChars)
                listOfChars = []
            reversedLine += currentChar
            
    #clean up any leftovers at the end of the line
    if len(listOfChars) > 0:
        reversedLine += ReverseArray(listOfChars)
    return reversedLine




print ReverseLine("this! is? only a--test")