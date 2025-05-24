#!/usr/bin/python3
# Suhail Al-aboud
# 10675@holbertonstudents.com
"""
Solves the N queens problem and prints all solutions.
Usage: nqueens N
"""

import sys


def is_safe(queens, row, col):
    """
    Check if a queen can be placed at (row, col) safely.

    Args:
        queens (list): columns of already placed queens by row index.
        row (int): current row index.
        col (int): column to test.

    Returns:
        bool: True if safe, False otherwise.
    """
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == row - r:
            return False
    return True


def solve(n, row=0, queens=None):
    """
    Recursively place queens row by row and print each solution.

    Args:
        n (int): board size and number of queens.
        row (int): current row index.
        queens (list): columns of placed queens.
    """
    if queens is None:
        queens = []
    if row == n:
        solution = [[r, queens[r]] for r in range(n)]
        print(solution)
        return
    for col in range(n):
        if is_safe(queens, row, col):
            solve(n, row + 1, queens + [col])


def main():
    """
    Parse arguments, validate N, and run the solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(n)


if __name__ == "__main__":
    main()
