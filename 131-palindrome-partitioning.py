""" 131. Palindrome Partitioning - Medium
topic: backtracking
related: 132. Palindrome Partitioning II - Hard

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
] """


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        current = []
        self.partitionRecursive(result, current, s, 0)
        return result

    def partitionRecursive(self, result, current, s, start):
        if start == len(s):
            result.append(list(current))
        else:
            for i in range(start, len(s)):
                if self.isPalindrome(s[start:i + 1]):
                    current.append(s[start:i + 1])
                    self.partitionRecursive(result, current, s, i + 1)
                    current.pop()

    def isPalindrome(self, substring):
        return substring == substring[::-1]


if __name__ == "__main__":
    res = Solution().partition(s='aab')
    print(res)
