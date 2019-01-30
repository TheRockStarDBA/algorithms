""" 67. Add Binary - Easy
Topic: string, math
Related:
Add Two Numbers - Medium
Multiply Strings - Medium
Plus One - Easy

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101" """


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        carry, val = 0, 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = val / 2, val % 2
            result += str(val)
        if carry:
            result += str(carry)

        return result[::-1]


if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a, b))
