""" 37. Sudoku Solver - Hard
# hash table, backtracking

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes
of the grid.
Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9. """


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


if __name__ == "__main__":
    sudoku = [
        "..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.",
        ".98...3..", "...8.3.2.", "........6", "...2759.."
    ]
