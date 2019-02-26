""" 87. Scramble String - Hard
topic: string, dynamic programming

Given a string s1, we may represent it as a binary tree by partitioning it to
two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a
scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it
produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled
string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false """

# Approach 1: Recursion
#   1) break the string to two parts:
#         s1[0:j]   s1[j+1:n]
#         s2[0:j]   s2[j+1:n]
#   2) then
#         isScramble(s1[0:j], s2[0:j]) and  isScramble(s1[j+1:n], s2[j+1:n])
#       OR
#         isScramble(s1[0:j], s2[j+1: n]) and  isScramble(s1[j+1:n], s2[0:j])

from collections import Counter


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2) or not s1 or not s2:
            return False
        if s1 == s2:
            return True

        c1 = Counter(s1)
        c2 = Counter(s2)
        if c1 != c2:
            return False

        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(
                    s1[i:], s2[i:])) or \
                (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(
                    s1[i:], s2[:len(s2) - i])):
                return True

        return False


# Approach 2: Dynamic Programming

#       dp[k][i][j] means:

#          a) s1[i] start from 'i'
#          b) s2[j] start from 'j'
#          c) 'k' is the length of substring

#   Initialization

#       dp[1][i][j] = (s1[i] == s2[j])

#   Formula

#       same as the above recursive method idea

#       dp[k][i][j] =
#           dp[divk][i][j] and dp[k-divk][i+divk][j+divk] or
#           dp[divk][i][j+k-divk] and dp[k-divk][i+divk][j]

#       `divk` mean split the k to two parts, so 0 <= divk <= k;


class Solution2(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2) or not s1 or not s2:
            return False
        if s1 == s2:
            return True

        n = len(s1)
        # create dp[n+1][n][n] matrix
        dp = [[[False for j in range(n)] for i in range(n)]
              for k in range(n + 1)]
        # initiate dp matrix
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = (s1[i] == s2[j])

        for k in range(2, n + 1):
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    for divk in range(1, k):
                        if ( dp[divk][i][j] and dp[k-divk][i+divk][j+divk] ) or \
                            ( dp[divk][i][j+k-divk] and dp[k-divk][i+divk][j] ):
                            dp[k][i][j] = True

        return dp[n][0][0]


if __name__ == "__main__":
    s1 = "great"
    s2 = "rgeat"
    ans = Solution().isScramble(s1, s2)
    print(ans)
    s3 = "abcde"
    s4 = "caebd"
    ans2 = Solution().isScramble(s3, s4)
    print(ans2)