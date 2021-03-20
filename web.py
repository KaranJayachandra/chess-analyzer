from requests import get
import chess.pgn
import os

def getGames(userName, gamesDate, fileName):
    currentPeriod = gamesDate.strftime("%Y")+'/'+gamesDate.strftime("%m")
    currentDate = gamesDate.strftime("%Y.%m.%d")
    startString = 'https://api.chess.com/pub/player/' + userName + '/games/'
    endString = '/pgn'
    requestString = startString + currentPeriod + endString
    response = get(requestString)
    outputFile = open(fileName, 'w')
    outputFile.write(response.text)
    outputFile.close()
    cleanGames(currentDate, fileName)

def cleanGames(currentDate, fileName):
    currentGames = []
    pgn = open(fileName)
    while True:
        game = chess.pgn.read_game(pgn)
        if game == None:
            break 
        else:
            if game.headers["Date"] == currentDate:
                currentGames.append(game)
    pgn.close()
    if os.path.exists(fileName):
        os.remove(fileName)
    for game in currentGames:
        print(game, file=open(fileName, 'a'), end='\n\n')

def getDescription(fileName):
    currentGames = []
    pgn = open(fileName)
    while True:
        game = chess.pgn.read_game(pgn)
        if game == None:
            break
        else:
            white = game.headers["White"]
            black = game.headers["Black"]
            description = white + ' vs. ' + black
            currentGames.append(description)
    pgn.close()
    return currentGames