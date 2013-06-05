__author__ = 'tina'


def PrintStarSquare(n):
    """ Prints a square of stars, where each side has a size of n. N must be >= 3 """
    if n < 3:
        raise ValueError('n must be >= 3')

    #   Prints a square of stars, where each side has a size of n.
    totalRowLength = n

    # if n is odd, the max width of the diamond that goes inside it will be the next smallest odd number.
    # the definition of "next smallest odd number" is not some weird formula that divides and adds and re-multiplies -
    #   it's (number - 2)
    # if n is even, the max width of the diamond will be X -1, then use the previous formula.
    tempRowLength = n

    if n % 2 == 0:
        tempRowLength -= 1

    maxDiamondWidth = tempRowLength - 2

    #now we know how long the row is, and how wide the diamond is at it's widest point.
    # It wasn't specified, but even numbers will have an extra star on the right and bottom.
    currentDiamondWidth = 0
    countingDirection = 1   # +1 for counting up, -1 for counting down.

    for rowCounter in range(totalRowLength):
        if currentDiamondWidth == 0:
            thisRowString = "*" * totalRowLength
        else:
            leftStars = (totalRowLength - currentDiamondWidth) / 2
            rightStars = totalRowLength - leftStars - currentDiamondWidth
            thisRowString = ("*" * leftStars) + (" " * currentDiamondWidth) + ("*" * rightStars)
        print(thisRowString)

        if currentDiamondWidth == maxDiamondWidth:
            countingDirection *= -1

        if currentDiamondWidth == 0:
            if countingDirection == 1:
                currentDiamondWidth += 1
            else:
                currentDiamondWidth = 0 #never go below 0
        elif currentDiamondWidth == 1:  # we can only go to 0, we don't want to subtract 2
            if countingDirection == 1:
                currentDiamondWidth +=2
            else:
                currentDiamondWidth = 0
        else:
            currentDiamondWidth += 2 * countingDirection



for i in range(3,15):
    print "--- %d ---" % i
    PrintStarSquare(i)
