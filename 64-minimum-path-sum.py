""" 64. Minimum Path Sum - Medium

topic: array, dynamic programming
related:  Unique Paths - Medium
          Dungeon Game - Hard
          Cherry Pickup - Hard

Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum. """

#dynamic programming


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        dp = list(grid[0])
        for j in range(1, col):
            dp[j] += dp[j - 1]

        for i in range(1, row):
            dp[0] += grid[i][0]
            for j in range(1, col):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = Solution().minPathSum(grid)
    print(result)