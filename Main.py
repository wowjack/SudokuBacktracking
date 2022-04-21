from pygame import *
import Solver, UI, Cell, sys, gameBoard

init()

'''
Works great. Solve speed can be changed by changing the number of loops exist inside of the solve function.
Maybe make random button that pulls a puzzle off of websudoku.
'''

class main:
    def __init__(self):
        self.window = display.set_mode((800,900))
        self.windowColor = (255,255,255)
        display.set_caption("Sudoku Solver")
        self.uiElements = []
        self.uiRect = Rect((0,0), (800,100))
        self.uiBar = self.window.subsurface(self.uiRect)
        self.solveButton = UI.Button("Solve", (140,70), 50, (700,50), self.uiBar)
        self.uiElements.append(self.solveButton)
        self.clearButton = UI.Button("Clear", (140,70), 50, (550,50), self.uiBar)
        self.uiElements.append(self.clearButton)
        self.checkButton = UI.Button("Check", (140,70), 50, (100,50), self.uiBar)
        self.uiElements.append(self.checkButton)

        self.boardRect = Rect((63,163), (675,675))
        self.boardSurf = self.window.subsurface(self.boardRect)
        self.board = gameBoard.Board(self.boardSurf)
        self.s = Solver.SudokuSolver(self.board)

    def update(self, events):
        self.window.fill(self.windowColor)
        self.uiBar.fill((200,200,200))
        self.boardSurf.fill((200,200,200))
        self.board.update(events)
        for element in self.uiElements:
            element.update(events)
        self.drawLines()
        self.s.update()
        if self.solveButton.isClicked(events):
            self.s.solveinit(self.board)
            self.windowColor = (255,255,255)
        if self.clearButton.isClicked(events):
            self.board.clear()
            self.windowColor = (255,255,255)
        if self.checkButton.isClicked(events):
            if self.board.check():
                self.windowColor = (0,255,0)
            else:
                self.windowColor = (255,0,0)

    def drawLines(self):
        for x in range(1,675):
            if x % 225 == 0:
                draw.line(self.boardSurf, (0,0,0), (x,0), (x,675), 7)
        for y in range(1,675):
            if y % 225 == 0:
                draw.line(self.boardSurf, (0,0,0), (0,y), (675,y), 7)

m = main()
clock = time.Clock()
while True:
    allEvents = event.get()
    m.update(allEvents)
    for e in allEvents:
        if e.type == QUIT:
            quit()
            sys.exit()

    display.update()
