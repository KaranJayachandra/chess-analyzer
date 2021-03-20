import chess
import chess.pgn
import chess.engine
import matplotlib

def evalGame(game, evalDepth):
    engine = chess.engine.SimpleEngine.popen_uci('stockfish')
    board = game.board()
    analysis = []
    for move in game.mainline_moves():
        board.push(move)
        info = engine.analyse(board, chess.engine.Limit(depth=evalDepth))
        analysis.append(info['score'].white().score(mate_score=10000))
    engine.quit()
    return analysis

def analyzeGames(fileName, evalDepth):
    evaluations = []
    pgn = open(fileName)
    while True:
        game = chess.pgn.read_game(pgn)
        if game == None:
            break 
        else:
            evaluations.append(evalGame(game, evalDepth))
    return evaluations

'''
def makePlot(evaluations, descriptions):
    for index in range(len(evaluations)):
        evaluation = evaluations[index]
        description = descriptions[index]
        pyplot.plot(range(len(evaluation)), evaluation, label = description)
    pyplot.legend()
    pyplot.grid(which='both', axis='both')
    pyplot.xlabel('Moves')
    pyplot.ylabel('Centipawn')
    pyplot.ylim((-10000, 10000))
    pyplot.show()
'''

def getPlot(evaluations, descriptions):
    plotFigure = matplotlib.figure.Figure(figsize=(5, 5), dpi=100)
    pyplot = plotFigure.add_subplot(111)
    for index in range(len(evaluations)):
        evaluation = evaluations[index]
        description = descriptions[index]
        pyplot.plot(range(len(evaluation)), evaluation, label = description)
    pyplot.legend()
    pyplot.grid(which='both', axis='both')
    pyplot.set_xlabel('Moves')
    pyplot.set_ylabel('Centipawn')
    pyplot.set_ylim((-10000, 10000))
    return plotFigure