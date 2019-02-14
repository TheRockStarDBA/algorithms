""" 50. Pow(x, n) - Medium
topic: binary search, math
related: Sqrt(x) - Easy
        Super Pow - Medium

Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2^(-2) = 1/2^2 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
 """

# Time:  O(logn) = O(1)
# Space: O(1)


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        abs_n = abs(n)
        while abs_n:
            if abs_n & 1:
                result *= x
            abs_n >>= 1
            x *= x

        return 1 / result if n < 0 else result


if __name__ == "__main__":
    print(Solution().myPow(2.00000, -2))
    print(Solution().myPow(2.10000, 3))