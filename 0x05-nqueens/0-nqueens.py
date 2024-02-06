#!/usr/bin/python3
# 0-nqueens.py
# HAJAR EL ABDELLAOUI
"""Program that solve the N queen challenge"""
import sys


class SolveNQueens():
    """Definition of SolveNQueens class"""

    def __init__(self, n):
        self.n = n
        self.board = [[" "] * n for i in range(n)]

        self.cols = set()        # Used columns
        self.rightDiag = set()   # Used right Diagonals
        self.leftDiag = set()    # Used left Diagonals

        self.solutions = []     # list of existing solutions

    def backtrack(self, row=0):
        if row == self.n:
            result = []
            for row in self.board:
                [result.append(pos) for pos in row if pos != " "]
            self.solutions.append(result)
            return

        for col in range(self.n):
            if (col in self.cols or
                    (row + col) in self.rightDiag or
                    (row - col) in self.leftDiag):
                continue

            self.cols.add(col)
            self.rightDiag.add(row + col)
            self.leftDiag.add(row - col)
            self.board[row][col] = [row, col]

            self.backtrack(row + 1)

            self.cols.remove(col)
            self.rightDiag.remove(row + col)
            self.leftDiag.remove(row - col)
            self.board[row][col] = " "

    def solve(self):
        self.backtrack()
        for solution in self.solutions:
            print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    n_queens = SolveNQueens(N)
    n_queens.solve()
