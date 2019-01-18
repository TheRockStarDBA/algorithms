"""
22. Generate Parentheses

Topics: string, backtracking, recursion (medium level)
Similar Questions: Letter Combinations of a Phone Number (Medium); Valid Parentheses (Easy)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
] """

# Approach: Backtracking

# Add '(' or ')' when we know it will remain a valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so far.

# We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return ans


print(Solution().generateParenthesis(3))