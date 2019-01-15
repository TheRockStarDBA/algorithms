""" 38. Count and Say

Topic: string (easy level)

Encode and Decode Strings (Medium)
String Compression (Easy)

Description:
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211" """
""" The following are the terms from n=1 to n=10 of the count-and-say sequence:
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211

To generate the nth term, just count and say the n-1th term. """
import re
import itertools


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # straightforward approach
        s = '1'
        for _ in range(n - 1):
            cur = s[0]
            counter = 0
            temp = ''
            for char in s:
                if char == cur:
                    counter += 1
                else:
                    temp += str(counter) + cur
                    cur = char
                    counter = 1
            temp += str(counter) + cur
            s = temp

        return s

    def countAndSay1(self, n):
        """
        :type n: int
        :rtype: str
        """
        # using regular expression
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1),
                       s)
        return s

    def countAndSay2(self, n):
        """
          :type n: int
          :rtype: str
          """
        # using groupby

        s = '1'
        for _ in range(n - 1):
            s = ''.join(
                str(len(list(group))) + digit
                for digit, group in itertools.groupby(s))
        return s


print(Solution().countAndSay(4))
print(Solution().countAndSay1(5))
print(Solution().countAndSay2(6))