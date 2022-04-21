from pygame import *
import Cell

init()

class Board:
    def __init__(self,surface):
        self.board = [[],[],[],[],[],[],[],[],[]]
        self.surface = surface
        for row in range(9):
            for column in range(9):
                self.board[row].append(Cell.cell([row,column], self.surface))

    def update(self,events):
        for row in self.board:
            for column in row:
                column.update(events)

    def getNum(self, row, column):
        return self.board[row][column].num

    def setNum(self, row, column, number):
        self.board[row][column].num = number

    def getBox(self, row, column):
        numbers = []
        if row <= 2:
            y = 0
        elif row <= 5:
            y = 1
        else:
            y = 2
        if column <= 2:
            x = 0
        elif column <= 5:
            x = 1
        else:
            x = 2
        for i in range(3):
            for j in range(3):
                if [y*3+i, x*3+j] != [row,column]:
                    numbers.append(self.getNum(y*3+i,x*3+j))
        return numbers

    def getColumn(self, row, column):
        numbers = []
        for i in range(9):
            if i != row:
                numbers.append(self.getNum(i,column))
        return numbers

    def getRow(self, row, column):
        numbers = []
        for i in range(9):
            if i != column:
                numbers.append(self.getNum(row,i))
        return numbers

    def clear(self):
        for row in self.board:
            for column in row:
                column.clear()

    def checkDigit(self, row, column, digit):
        if digit > 9:
            return False
        checks = self.getRow(row,column) + self.getColumn(row,column) + self.getBox(row,column)
        for check in checks:
            if check == digit:
                return False
        return True

    def check(self):
        for row in range(9):
            for cell in range(9):
                if not self.checkDigit(row,cell,self.getNum(row,cell)):
                    return False
        return True
