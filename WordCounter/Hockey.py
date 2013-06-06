__author__ = 'Tina'
import csv

def AsNumber(score):
    score = score.strip()
    if not score.isdigit():
        raise ValueError("%s is not a number"%score)
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




scoreTable = {}
with open('hockey.csv', 'rb') as csvfile:
    myReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in myReader:
        PopulateDictionaryForRow(row, scoreTable)

print scoreTable
