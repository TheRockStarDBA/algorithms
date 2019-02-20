""" 76. Minimum Window Substring - Hard
Topic: hash table, two-pointers, string
Related:    Substring with Concatenation of All Words - Hard
            Minimum Size Subarray Sum - Medium
            Sliding Window Maximum - Hard
            Permutation in String - Medium
            Smallest Range - Hard
            Minimum Window Subsequence - Hard

Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty
string "".
If there is such window, you are guaranteed that there will always be only one
unique minimum window in S.
 """

from collections import Counter

# Time:  O(n)
# Space: O(k), k is the number of different characters


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        count_dict = Counter(t)

        # Number of unique characters in t,
        # which needs to be present in the desired window.
        unique_char = len(count_dict)

        # Dictionary which keeps a count of all the unique characters in the current window.
        current_count = {}

        start, end = 0, 0

        min_width, min_start = float("inf"), 0

        # keep track of how many unique characters in t are present in the current
        # window in its desired frequency
        curr_unique = 0

        while end < len(s):
            char = s[end]
            current_count[char] = current_count.get(char, 0) + 1

            if char in count_dict and current_count[char] == count_dict[char]:
                curr_unique += 1

            while start <= end and curr_unique == unique_char:
                char = s[start]

                if end - start + 1 < min_width:
                    min_width = end - start + 1
                    min_start = start

                # character at the position pointed by the `left` pointer is
                # no longer a part of the window.
                current_count[char] -= 1
                if char in count_dict and current_count[char] < count_dict[
                        char]:
                    curr_unique -= 1

                # move the left pointer ahead and look for a new window.
                start += 1

            # keep expanding the window once we are done contracting.
            end += 1

        if min_width == float("inf"):
            return ""

        return s[min_start:min_start + min_width]


if __name__ == "__main__":
    result = Solution().minWindow(s="ADOBECODEBANC", t="ABC")
    print(result)
