from datetime import date, datetime
from web import getGames, cleanGames, getDescription
from analyze import evalGame, analyzeGames, makePlot
import PySimpleGUI as gui

fileName = 'temp.pgn'

layout = [  [gui.Text('Enter your Chess.com username:'), gui.InputText()],
            [gui.Text('Enter the date of chess games'), gui.InputText(), gui.CalendarButton('Choose Date')],
            [gui.Button('Plot'), gui.Button('Close')]   ]
window = gui.Window('Chess.com Analyzer', layout)

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Close':
        break
    userName = values[0]
    today = datetime.strptime(values[1], '%Y-%m-%d %H:%M:%S')
    currentPeriod = today.strftime("%Y")+'/'+today.strftime("%m")
    currentDate = today.strftime("%Y.%m.%d")
    getGames(userName, currentPeriod, fileName)
    cleanGames(currentDate, fileName)
    evaluations = analyzeGames(fileName, 10)
    descriptions = getDescription(fileName)
    makePlot(evaluations, descriptions)

window.close()