""" 72. Edit Distance - Hard
topic: string, dynamic programming
related:    One Edit Distance - Medium
            Delete Operation for Two Strings - Medium
            Minimum ASCII Delete Sum for Two Strings - Medium

Given two words word1 and word2, find the minimum number of operations required
to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 """

#
#   Dynamic Programming Approach
#
#
#   dp[i][j] is minimal distance from word1[0..i] to word2[0..j]
#
#       1) if word1[i] == word2[j], then dp[i][j] == dp[i-1][j-1].
#
#       2) if word1[i] != word2[j], then we need to find which one below is minimal:
#
#              min( dp[i-1][j-1], dp[i-1][j],  dp[i][j-1] )
#
#              and +1 - current char need be changed.
#
#       Let's take a look  dp[1][2] :  "a" => "ab"
#
#                 +---+  +---+
#          ''=> a | 1 |  | 2 | '' => ab
#                 +---+  +---+
#
#                 +---+  +---+
#          a => a | 0 |  | 1 | a => ab
#                 +---+  +---+
#
#  To know the minimal distance `a => ab`, we can get it from one of the following cases:
#
#              1) delete the last char in word1,  minDistance( '' => ab ) + 1
#              2) delete the last char in word2,  minDistance(  a => a ) + 1
#              3) change the last char,           minDistance( '' => a ) + 1
#
#
#       For Example:
#
#          word1="abb", word2="abccb"
#
#          1) Initialize the DP matrix as below:
#
#                 "" a b c c b
#              "" 0  1 2 3 4 5
#              a  1
#              b  2
#              b  3
#
#          2) Dynamic Programming
#
#                 "" a b c c b
#              ""  0 1 2 3 4 5
#              a   1 0 1 2 3 4
#              b   2 1 0 1 2 3
#              b   3 2 1 1 2 2
#


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(n + 1):
            dp[i][0] = i

        for row in range(1, n + 1):
            for col in range(1, m + 1):
                if word1[col - 1] == word2[row - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    minVal = min(dp[row - 1][col - 1], dp[row - 1][col],
                                 dp[row][col - 1])
                    dp[row][col] = minVal + 1

        return dp[n][m]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    distance = Solution().minDistance(word1, word2)
    print(distance)
