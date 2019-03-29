""" 200. Number of Islands - Medium

#depth-first-search, breadth-first-search, union-find

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

RELATED:
Surrounded Regions - Medium
Walls and Gates - Medium
Number of Islands II - Hard
Number of Connected Components in an Undirected Graph - Medium
Number of Distinct Islands - Medium
Max Area of Island - Medium

"""

# Time:  O(m * n)
# Space: O(m * n)


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        row, col = len(grid), len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, row, col, i, j)
                    count += 1
        return count

    def dfs(self, grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'
        if x != 0:
            self.dfs(grid, row, col, x - 1, y)
        if x != row - 1:
            self.dfs(grid, row, col, x + 1, y)
        if y != 0:
            self.dfs(grid, row, col, x, y - 1)
        if y != col - 1:
            self.dfs(grid, row, col, x, y + 1)


if __name__ == "__main__":
    grid = [["1", "1", "0", "0", "0"], ["0", "1", "0", "0", "1"],
            ["1", "0", "0", "1", "1"], ["0", "0", "0", "0", "0"],
            ["1", "0", "1", "0", "1"]]
    print(Solution().numIslands(grid))
