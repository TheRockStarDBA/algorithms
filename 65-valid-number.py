""" 65. Valid Number - Hard
topic: string, array
related: 8. String to Integer (atoi) - Medium

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather
all requirements up front before implementing one. However, here is a list of
characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        idx = 0
        n = len(s)

        if n == 0:
            return False
        if s[idx] == "+" or s[idx] == '-':
            idx += 1

        isNumeric = False
        while idx < n and s[idx].isdigit():
            idx += 1
            isNumeric = True
        if idx < n and s[idx] == '.':
            idx += 1
            while idx < n and s[idx].isdigit():
                idx += 1
                isNumeric = True
        if idx < n and s[idx] == 'e' and isNumeric:
            isNumeric = False
            idx += 1
            if idx < n and (s[idx] == '+' or s[idx] == '-'):
                idx += 1
            while idx < n and s[idx].isdigit():
                idx += 1
                isNumeric = True

        if idx == n and isNumeric:
            return True
        return False


if __name__ == "__main__":
    print(Solution().isNumber("3.e-23"))
    print(Solution().isNumber(".2e81"))
    print(Solution().isNumber("2e10"))
    print(Solution().isNumber(" 0.1"))
    print(Solution().isNumber("1 b"))
    print(Solution().isNumber("3-2"))
    print(Solution().isNumber("abc"))
    print(Solution().isNumber("46.e19"))
