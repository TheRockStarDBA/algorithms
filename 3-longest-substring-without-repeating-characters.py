""" 3. Longest Substring Without Repeating Characters - Medium

topic: hash table, two pointers, string
related: Longest Substring with At Most Two Distinct Characters - Hard

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Note that the answer must be a substring, "pwke" is a subsequence and not a substring. """

# Hashmap Approach:
# Time:  O(n)
# Space: O(1)

# Commonly used character tables are:
# int[26] for Letters 'a' - 'z' or 'A' - 'Z'
# int[128] for ASCII
# int[256] for Extended ASCII


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        longest, start = 0, 0
        visited = [False for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)

        return longest


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
