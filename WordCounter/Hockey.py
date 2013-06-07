__author__ = 'Tina'
import csv


def AsNumber(score):
    score = score.strip()
    if not score.isdigit():
        raise ValueError("%s is not a number" % score)
    return int(score)


def AddTeamIfNotExists(teamName, scoreTable):
    if not teamName in scoreTable:
        scoreTable[teamName] = {}
        scoreTable[teamName]["played"] = []
        scoreTable[teamName]["score"] = 0


def AddTeamMatchup(team1, team2, scoreTable):
    if team2 in scoreTable[team1]:
        raise ValueError("%s played %s more then once" % (team1, team2))
    else:
        scoreTable[team1]["played"].append(team2)

    if team1 in scoreTable[team1]:
        raise ValueError("%s played %s more then once" % (team2, team1))
    else:
        scoreTable[team2]["played"].append(team1)


def PopulateDictionaryForRow(row, scoreTable):
    if len(row) != 4:
        raise ValueError("CSV format error.  Each row must contain exactly 4 columns.")

    team1 = row[0].strip()
    score1 = AsNumber(row[1])
    team2 = row[2].strip()
    score2 = AsNumber(row[3])

    AddTeamIfNotExists(team1, scoreTable)
    AddTeamIfNotExists(team2, scoreTable)

    #scoring.  2 points for a victory, 1 point for a tie
    if score1 > score2:
        scoreTable[team1]["score"] += 2
    elif score1 == score2:
        scoreTable[team1]["score"] += 1
        scoreTable[team2]["score"] += 1
    else:
        scoreTable[team2]["score"] += 2

    # who have we played?
    AddTeamMatchup(team1, team2, scoreTable)

def ReadInCSVFile(fileName, scoreTable):
    with open(fileName, 'rb') as csvfile:
        myReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in myReader:
            PopulateDictionaryForRow(row, scoreTable)

def CheckForMissingGames(scoreTable):
    for team in scoreTable:
        if len(scoreTable[team]["played"]) != len(scoreTable) - 1:
            print ("%s is missing games" % team)

def BuildPlaceTable(scoreTable, placeTable):
    for team in scoreTable:
        score = scoreTable[team]["score"]

        if not score in placeTable:
            placeTable[score] = []

        placeTable[score].append(team)

def FigureOutPlaces(scoreTable):
    placeTable = {}
    BuildPlaceTable(scoreTable, placeTable)
    keylist = placeTable.keys()
    keylist.sort(reverse=True)

    #for key in keylist:
    #    print "Wins: %d.  Teams: %s" % (key, ", ".join(placeTable[key] ))

    numTeamsPlaced = 0
    keyIndex = 0
    while numTeamsPlaced < 3 and keyIndex < len(keylist):
        if (numTeamsPlaced == 0):
            print "First Place: %s" % ", ".join(placeTable[keylist[keyIndex]])
        elif (numTeamsPlaced == 1):
            print "Second Place: %s" % ", ".join(placeTable[keylist[keyIndex]])
        elif (numTeamsPlaced == 2):
            print "Third Place: %s" % ", ".join(placeTable[keylist[keyIndex]])
        numTeamsPlaced += len(placeTable[keylist[keyIndex]])
        keyIndex += 1

scoreTable = {}
ReadInCSVFile("hockey.csv", scoreTable)
CheckForMissingGames(scoreTable)
FigureOutPlaces(scoreTable)