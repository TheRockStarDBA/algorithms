""" 28. Implement strStr() - Easy
topics: string, two-pointers, KMP-algorithm
related: 214. Shortest Palindrome - Hard
        459. Repeated Substring Pattern - Easy

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf(). """

# KMP algorithm
# Time:  O(n + k)
# Space: O(k)


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1

        k = len(needle)
        n = len(haystack)

        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        lps = [0] * k
        j = 0  # index for needle[]

        # Preprocess the pattern (calculate lps[] array)
        self.computeLPSArray(needle, k, lps)

        i = 0  # index for haystack[]
        while i < n:
            if needle[j] == haystack[i]:
                i += 1
                j += 1

            if j == k:
                return (i - j)  # Found pattern at index i-j

            # mismatch after j matches
            elif i < n and needle[j] != haystack[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    def computeLPSArray(self, pattern, k, lps):
        len = 0  # length of the previous longest prefix suffix

        lps[0]  # lps[0] is always 0
        i = 1

        # the loop calculates lps[i] for i = 1 to k-1
        while i < k:
            if pattern[i] == pattern[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len - 1]

                    # Also, note that we do not increment i here
                else:
                    lps[i] = 0
                    i += 1


if __name__ == "__main__":
    print(Solution().strStr(haystack="hello", needle="ll"))
    print(Solution().strStr(haystack="aaaaa", needle="bba"))
