""" 62. Unique Paths - Medium
Topic: array, dynamic programming
Related:    63. Unique Paths II - Medium
            64. Minimum Path Sum - Medium
            174.Dungeon Game - Hard
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the
diagram below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

 *    start                                                  
 *    +---------+----+----+----+----+----+
 *    |----|    |    |    |    |    |    |
 *    |----|    |    |    |    |    |    |
 *    +----------------------------------+
 *    |    |    |    |    |    |    |    |
 *    |    |    |    |    |    |    |    |
 *    +----------------------------------+
 *    |    |    |    |    |    |    |----|
 *    |    |    |    |    |    |    |----|
 *    +----+----+----+----+----+---------+
 *                                   finish

How many possible unique paths are there?

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28 """

# Approach: Dynamic Programming

# We have a dp[i][j] represents  how many paths from [0][0] to current location.
#     dp[i][j] =  1  if i==0 or j==0        //the first row/column only have 1 uniqe path.
#              =  dp[i-1][j] + dp[i][j-1]   //the path can be from my top cell and left cell.


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp_matrix = [1] * (m * n)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp_matrix[i * n + j] = 1
                else:
                    dp_matrix[i * n + j] = dp_matrix[
                        (i - 1) * n + j] + dp_matrix[i * n + j - 1]

        return dp_matrix[m * n - 1]


if __name__ == "__main__":
    print(Solution().uniquePaths(m=3, n=2))
    print(Solution().uniquePaths(m=7, n=3))
