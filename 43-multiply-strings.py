""" 43. Multiply Strings

Topic: Math, String (Medium Level)
Similar Questions:
2.Add Two Numbers (Medium); 66. Plus One (Easy);
67. Add Binary (Easy); 415. Add Strings (Easy)

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly. """


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        m = len(num1)
        n = len(num2)
        ret = [0] * (m + n)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1
                total = mul + ret[p2]

                ret[p1] += total // 10
                ret[p2] = (total) % 10

        start = 0
        while start < len(ret) and ret[start] == 0:
            start += 1

        result = ''.join(str(num) for num in ret[start:])

        return result if result else '0'


if __name__ == "__main__":
    num1 = "123"
    num2 = "456"
    print(Solution().multiply(num1, num2))