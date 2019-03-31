""" 171. Excel Sheet Column Number - Easy

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
 """


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res *= 26
            res += ord(s[i]) - ord('A') + 1

        return res


if __name__ == "__main__":
    res = Solution().titleToNumber("ZY")
    print(res)
