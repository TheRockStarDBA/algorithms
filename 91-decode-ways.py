""" 91. Decode Ways - Medium
topic: string, dynamic programming
related: 639. Decode Ways II - Hard

A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of
ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6). """

import string


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return self.iszero(s[0])

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = self.iszero(s[0])
        dp[1] = self.iszero(s[0]) * self.iszero(s[1]) + self.check(s[0], s[1])
        for i in range(2, len(s)):
            if (self.iszero(s[i])):
                dp[i] = dp[i - 1]
            if (self.check(s[i - 1], s[i])):
                dp[i] += dp[i - 2]
        return dp[len(s) - 1]

    def iszero(self, char):
        # check wether string character is 0 or not
        return 0 if (not char.isdigit() or char == '0') else 1

    def check(self, char1, char2):
        # check if the digit letter is between 10 and 26
        return 1 if (char1 == '1' or (char1 == '2' and char2 <= '6')) else 0


if __name__ == "__main__":
    print(Solution().numDecodings("12"))
    print(Solution().numDecodings("226"))
