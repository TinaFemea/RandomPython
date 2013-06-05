__author__ = 'tina'

def ReverseArray(listOfChars):
    reversedString = ""
    listOfChars.reverse()
    for reversedChar in listOfChars:
        reversedString += reversedChar
    return reversedString


def ReverseLine(inputLine):
    listOfChars = []
    reversedLine = ""
    for currentChar in inputLine:
        if currentChar.isalpha():
            listOfChars.append(currentChar)
        else:
            if len(listOfChars) > 0:
                reversedLine += ReverseArray(listOfChars)
                listOfChars = []
            reversedLine += currentChar

    if len(listOfChars) > 0:
        reversedLine += ReverseArray(listOfChars)
    return reversedLine




print ReverseLine("this! is? only a--test")