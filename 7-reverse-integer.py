""" 7. Reverse Integer - Easy
Topic: math
Related: String to Integer (atoi) - Medium
        Reverse Bits - Easy

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this
problem, assume that your function returns 0 when the reversed integer overflows. """

# Time:  O(1)
# Space: O(1)


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = None
        string_x = str(x)
        if string_x[0] == '-':
            sign = '-'
            string_x = string_x[1:]
        reversed_x = string_x[::-1]
        reversed_x = sign + reversed_x if sign else reversed_x
        result = int(reversed_x)
        if result > 2**31 - 1 or result < -2**31:
            return 0

        return result


class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
            flag = -1
        else:
            flag = 1
        x *= flag
        rev = 0
        while x:
            # pop operation:
            pop = x % 10
            x //= 10
            # push operation:
            rev = rev * 10 + pop

        if rev > 2147483647:
            return 0
        else:
            return rev * flag


if __name__ == "__main__":
    print(Solution().reverse(-123))
    print(Solution2().reverse(120))