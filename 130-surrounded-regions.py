""" 130. Surrounded Regions - Medium
topic: depth-first-search, breadth-first-search, union find
related: Number of Islands - Medium
        Walls and Gates - Medium

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the
border of the board are not flipped to 'X'. Any 'O' that is not on the border
and it is not connected to an 'O' on the border will be flipped to 'X'. Two
cells are connected if they are adjacent cells connected horizontally or vertically.
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board[0])
        n = len(board)

        queue = []

        for i in range(n):
            for j in range(m):
                if (i in (0,
                          n - 1)) or (j in (0, m - 1)) and board[i][j] == 'O':
                    queue.append((i, j))

        while queue:
            i, j = queue.pop()
            if 0 <= i < n and 0 <= j < m and board[i][j] == 'O':
                board[i][j] = 'M'
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < n and 0 <= y < m and board[x][y] == 'O':
                        queue.append((x, y))

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


if __name__ == "__main__":
    board = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    Solution().solve(board)
    print(board)