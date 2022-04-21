from pygame import *
import math, gameBoard, sys

class SudokuSolver:
    def __init__(self,board):
        self.board = board
        self.blanks = []
        self.blankPos = 0
        self.numCheck = 1
        self.solving = False

    def update(self):
        if self.solving:
            self.solve()

    def solveinit(self,board):
        self.blanks = self.blankSpaces(board)
        self.solving = True

    def checkDigit(self, row, column, digit):
        if digit > 9:
            return False
        checks = self.board.getRow(row,column) + self.board.getColumn(row,column) + self.board.getBox(row,column)
        for check in checks:
            if check == digit:
                return False
        return True

    def solve(self):
        for x in range(1000):
            if self.blankPos < len(self.blanks) and self.solving:
                if self.numCheck > 9:
                    self.board.setNum(self.blanks[self.blankPos][0], self.blanks[self.blankPos][1], 0)
                    self.blankPos -= 1
                    self.numCheck = self.board.getNum(self.blanks[self.blankPos][0], self.blanks[self.blankPos][1])
                elif self.checkDigit(self.blanks[self.blankPos][0], self.blanks[self.blankPos][1], self.numCheck):
                    self.board.setNum(self.blanks[self.blankPos][0], self.blanks[self.blankPos][1], self.numCheck)
                    self.numCheck = 0
                    self.blankPos += 1
                self.numCheck += 1
            elif self.solving:
                self.solving = False
                self.blankPos = 0
                self.numCheck = 1

    def blankSpaces(self,board):
        numbers = []
        for row in range(9):
            for column in range(9):
                if board.getNum(row, column) == 0:
                    numbers.append([row,column])
        return numbers
