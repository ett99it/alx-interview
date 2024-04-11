#!/usr/bin/python3
"""N queens solution finder module.

Usage: nqueens N:
    If the user called the program with the wrong number of arguments, print
        Usage: nqueens N, followed by a new line, and exit with the status 1.
where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a new line,
    and exit with the status 1.
    If N is smaller than 4, print N must be at least 4, followed by a new
    line, and exit with the status 1.
The program should print every possible solution to the problem.
    One solution per line.
    Format: see README.
    You don’t have to print the solutions in a specific order.
You are only allowed to import the sys module.
"""
import sys


def n_queens(n):
    """ N queens solution """
    queens, res = [], []
    cols, positive_diag, negative_diag = set(), set(), set()

    def backtrack(row, n, queens):
        """ Backtracking function """
        if row == n:
            res.append(queens[:])
            return
        for col in range(n):
            if (col in cols or row + col in positive_diag or
                    row - col in negative_diag):
                continue
            cols.add(col)
            positive_diag.add(row + col)
            negative_diag.add(row - col)
            queens.append([row, col])
            backtrack(row + 1, n, queens)

            cols.remove(col)
            positive_diag.remove(row + col)
            negative_diag.remove(row - col)
            queens.pop()
    backtrack(0, n, queens)
    return res


def check_args(n):
    """ Check if n is a valid argument """
    if not n.isdigit():
        print("N must be a number")
        exit(1)
    if int(n) < 4:
        print("N must be at least 4")
        exit(1)


def main():
    """ Main function """
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        exit(1)
    n = args[1]
    check_args(n)
    solutions = n_queens(int(n))
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()