""" 79. Word Search - Medium
topic: array, backtracking
related: Word Search II - Hard

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 """

# Recursive backtracking algorithm


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        mask = [[False for j in range(col)] for i in range(row)]

        for i in range(row):
            for j in range(col):
                if self.Recursive(board, word, 0, i, j, row, col, mask):
                    return True

        return False

    def Recursive(self, board, word, cur, i, j, row, col, mask):

        if cur == len(word):
            return True
        if i < 0 or i >= row or j < 0 or j >= col or mask[i][
                j] or board[i][j] != word[cur]:
            return False

        mask[i][j] = True
        result = \
            self.Recursive(board, word, cur + 1, i + 1, j, row, col, mask) or \
            self.Recursive(board, word, cur + 1, i - 1, j, row, col, mask) or \
            self.Recursive(board, word, cur + 1, i, j + 1, row, col, mask) or \
            self.Recursive(board, word, cur + 1, i, j - 1, row, col, mask)
        mask[i][j] = False

        return result


if __name__ == "__main__":
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    print(Solution().exist(board, word="ABCCED"))
    print(Solution().exist(board, word="SEE"))
    print(Solution().exist(board, word="ABCB"))
