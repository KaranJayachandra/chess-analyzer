from datetime import datetime
from web import getGames, getDescription
from analyze import evalGame, analyzeGames, getDayPlot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import Tk, ttk, Label, LabelFrame, Entry, Button, Listbox, SINGLE
from tkcalendar import Calendar

fileName = 'temp.pgn'

def getSummary():
    userName = userNameEntry.get()
    gamesDate = datetime.strptime(dateEntry.get_date(), '%m/%d/%y')
    getGames(userName, gamesDate, fileName)
    evaluations = analyzeGames(fileName, 10)
    descriptions = getDescription(fileName)
    plotFigure = getDayPlot(evaluations, descriptions)
    canvas = FigureCanvasTkAgg(plotFigure, master=resultsFrame)
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, resultsFrame, pack_toolbar=False)
    toolbar.update()
    
    canvas.get_tk_widget().grid(row=0, column=0)
    toolbar.grid(row=1, column=0)
    updateGameList(descriptions)


def updateGameList(descriptions):
    gameList = Listbox(analysisFrame, selectmode=SINGLE)
    for index in range(len(descriptions)):
        gameList.insert(index, descriptions[index])
        print(index, descriptions[index])
    gameList.pack()

root = Tk()
root.title('Chess.com Analyzer')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)

tabView = ttk.Notebook(root)
resultsFrame = LabelFrame(root, text='Results')

summaryFrame = ttk.Frame(tabView)
analysisFrame = ttk.Frame(tabView)
tabView.add(summaryFrame, text='Summary')
tabView.add(analysisFrame, text='Game')

tabView.grid(row=0, column=0)
resultsFrame.grid(row=0, column=1)

userNameLabel = Label(summaryFrame, text='Enter Username:')
dateLabel = Label(summaryFrame, text='Enter Date:')
userNameEntry = Entry(summaryFrame)
dateEntry = Calendar(summaryFrame, selectmode='day')
plotButton = Button(summaryFrame, text='Summary', command=getSummary)
closeButton = Button(summaryFrame, text='Close', command=root.quit)

userNameLabel = Label(summaryFrame, text='Enter Username:')
dateLabel = Label(summaryFrame, text='Enter Date:')
userNameEntry = Entry(summaryFrame)
dateEntry = Calendar(summaryFrame, selectmode='day')
plotButton = Button(summaryFrame, text='Summary', command=getSummary)
closeButton = Button(summaryFrame, text='Close', command=root.quit)

userNameLabel.grid(row=0, column=0)
dateLabel.grid(row=1, column=0)
userNameEntry.grid(row=0, column=1)
dateEntry.grid(row=1, column=1)
plotButton.grid(row=2, column=0)
closeButton.grid(row=2, column=1)

root.mainloop()