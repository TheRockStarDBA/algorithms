""" 32. Longest Valid Parentheses - Hard

Topic: string, dynamic programming
Related: 20. Valid Parentheses - Easy

Given a string containing just the characters '(' and ')', find the length of the 
longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()" """

# Approach 1: using Stack
# For every ‘(’ encountered, we push its index onto the stack.
# For every ‘)’ encountered, we pop the topmost element and subtract the current
# element's index from the top element of the stack, which gives the length of
# the currently encountered valid string of parentheses. If while popping the
# element, the stack becomes empty, we push the current element's index onto the
# stack. In this way, we keep on calculating the lengths of the valid substrings,
# and return the length of the longest valid string at the end.

# Time:  O(n)
# Space: O(n)


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxLength = 0
        last = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif not stack:
                last = i
            else:
                stack.pop()
                if not stack:
                    maxLength = max(maxLength, i - last)
                else:
                    maxLength = max(maxLength, i - stack[-1])
        return maxLength


if __name__ == "__main__":
    print(Solution().longestValidParentheses(")()())"))
    print(Solution().longestValidParentheses("(()))())("))