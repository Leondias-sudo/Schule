import urllib.request
import requests
import urllib
def teamA(spiel):
    return spiel['team1']['teamName']
def teamB(spiel):
    return spiel['team2']['teamName']
responseJson = requests.api.get('https://api.openligadb.de/getmatchdata/bl1/2023/0').json()
firstGame = responseJson[0]
lastGame = responseJson[len(responseJson)-1]
for match in responseJson:
    if teamA(match) == 'Werder Bremen':
        print(f"Spiel {teamA(match)} gegen {teamB(match)} {match['matchResults'][1]['pointsTeam1']} zu {match['matchResults'][1]['pointsTeam2']}")
    if teamB(match) == 'Werder Bremen':
        print(f"Spiel {teamA(match)} gegen {teamB(match)} {match['matchResults'][1]['pointsTeam1']} zu {match['matchResults'][1]['pointsTeam2']}")
print(f"Erstes Spiel {teamA(firstGame)} gegen {teamB(firstGame)} {firstGame['matchResults'][1]['pointsTeam1']} zu {firstGame['matchResults'][1]['pointsTeam2']}")
print(f"Letzes Spiel {teamA(lastGame)} gegen {teamB(lastGame)} {lastGame['matchResults'][1]['pointsTeam1']} zu {lastGame['matchResults'][1]['pointsTeam2']}")

