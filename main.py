from datetime import datetime
from web import getGames, getDescription
from analyze import evalGame, analyzeGames, getPlot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter
import tkcalendar

fileName = 'temp.pgn'

def getSummary():
    userName = userNameEntry.get()
    gamesDate = datetime.strptime(dateEntry.get_date(), '%m/%d/%y')
    getGames(userName, gamesDate, fileName)
    evaluations = analyzeGames(fileName, 10)
    descriptions = getDescription(fileName)
    plotFigure = getPlot(evaluations, descriptions)
    canvas = FigureCanvasTkAgg(plotFigure, master=resultsFrame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)
    toolbar = NavigationToolbar2Tk(canvas, resultsFrame)
    toolbar.update()
    canvas.get_tk_widget().grid(row=1, column=1)

root = tkinter.Tk()
root.title('Chess.com Analyzer')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=4)

tabView = tkinter.ttk.Notebook(root)
resultsFrame = tkinter.LabelFrame(root, text='Results')

summaryFrame = tkinter.ttk.Frame(tabView)
analysisFrame = tkinter.ttk.Frame(tabView)
tabView.add(summaryFrame, text='Summary')
tabView.add(analysisFrame, text='Game')

tabView.grid(row=0, column=0)
resultsFrame.grid(row=0, column=1)

userNameLabel = tkinter.Label(summaryFrame, text='Enter Username:')
dateLabel = tkinter.Label(summaryFrame, text='Enter Date:')
userNameEntry = tkinter.Entry(summaryFrame)
dateEntry = tkcalendar.Calendar(summaryFrame, selectmode='day')
plotButton = tkinter.Button(summaryFrame, text='Summary', command=getSummary)
closeButton = tkinter.Button(summaryFrame, text='Close', command=root.quit)

userNameLabel.grid(row=0, column=0)
dateLabel.grid(row=1, column=0)
userNameEntry.grid(row=0, column=1)
dateEntry.grid(row=1, column=1)
plotButton.grid(row=2, column=0)
closeButton.grid(row=2, column=1)

root.mainloop()