""" 44. Wildcard Matching - Hard
topic: string, dynamic programming, greedy, backtracking
related: 10. Regular Expression Matching - Hard

Given an input string (s) and a pattern (p), implement wildcard pattern matching
with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*'
matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false """


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p_idx, s_idx, last_p_idx, last_s_idx = 0, 0, -1, -1

        while s_idx < len(s):
            # regular matching with '?'
            if p_idx < len(p) and (s[s_idx] == p[p_idx] or p[p_idx] == "?"):
                s_idx += 1
                p_idx += 1

            # matching with '*'
            elif p_idx < len(p) and p[p_idx] == "*":
                p_idx += 1
                last_p_idx = p_idx
                last_s_idx = s_idx

            # Not matching, but there is a '*' in previous
            elif last_p_idx != -1:
                last_s_idx += 1
                s_idx = last_s_idx
                p_idx = last_p_idx

            # Not matching and there is no '*' in previous
            else:
                return False

        # Check if there is still character except '*' in the pattern
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1

        # If finish scanning both string and pattern, then it matches well
        return p_idx == len(p)


if __name__ == "__main__":
    print(Solution().isMatch(s="acdcb", p="a*c?b"))
    print(Solution().isMatch(s="adceb", p="*a*b"))
