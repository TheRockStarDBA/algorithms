""" 17. Letter Combinations of a Phone Number

Topics: String, Backtracking (Medium)
Related: 22. Generate Parentheses (Medium);
         39. Combination Sum (Medium)

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in
any order you want.
 """


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mapping = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return list(mapping[digits])

        else:
            start = list(mapping[digits[0]])
            for d in digits[1:]:
                current = list(mapping[d])
                start = [s + c for s in start for c in current]

            return start


if __name__ == "__main__":
    digits = '23'
    result = Solution().letterCombinations(digits)
    print(result)