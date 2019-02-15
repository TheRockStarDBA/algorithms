""" 6. ZigZag Conversion - Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for better
legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number
of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I """


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        step = 2 * numRows - 2
        zig = ''

        for i in range(numRows):
            for j in range(i, len(s), step):
                zig += s[j]
                if 0 < i < numRows - 1 and (j + step - 2 * i) < len(s):
                    zig += s[j + step - 2 * i]
        return zig


if __name__ == "__main__":
    result = Solution().convert(s="PAYPALISHIRING", numRows=3)
    print(result)