""" 10. Regular Expression Matching - Hard

topics: string, dynamic programming, backtracking
related: 44 wildcard matching - hard

Given an input string (s) and a pattern (p), implement regular expression matching
with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by
repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it
matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false """

# Approach 1: Recursion
# Algorithm

# If there were no Kleene stars (the * wildcard character for regular expressions),
# the problem would be easier - we simply check from left to right if each
# character of the text matches the pattern.

# When a star is present, we may need to check many different suffixes of the
# text and see if they match the rest of the pattern. A recursive solution is a
# straightforward way to represent this relationship.


class Solution(object):
    def isMatch(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], "."}

        if len(pattern) >= 2 and pattern[1] == "*":
            return (self.isMatch(text, pattern[2:])
                    or first_match and self.isMatch(text[1:], pattern))

        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


# Approach 2: Dynamic Programming
# Intuition

# As the problem has an optimal substructure, it is natural to cache intermediate
# results. We ask the question dp(i, j): does text[i:] and pattern[j:] match? We
# can describe our answer in terms of answers to questions involving smaller strings.

# Algorithm


# We proceed with the same recursion as in Approach 1, except because calls will
# only ever be made to match(text[i:], pattern[j:]), we use dp(i, j) to handle
# those calls instead, saving us expensive string-building operations and allowing
# us to cache the intermediate results.
class Solution2(object):
    def isMatch(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[0][0] = True
        for i in range(2, len(pattern) + 1):
            if pattern[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(text) + 1):
            for j in range(1, len(pattern) + 1):
                if pattern[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (
                        text[i - 1] == pattern[j - 1] or pattern[j - 1] == '.')
                else:
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and
                                                (text[i - 1] == pattern[j - 2]
                                                 or pattern[j - 2] == '.'))

        return dp[len(text)][len(pattern)]


if __name__ == "__main__":
    res = Solution().isMatch(text="mississippi", pattern="mis*is*p*.")
    print(res)