""" 30. Substring with Concatenation of All Words - Hard
topics: hash table, two pointers, string
related: Minimum Window Substring - Hard
You are given a string, s, and a list of words, words, that are all of the same
length. Find all starting indices of substring(s) in s that is a concatenation
of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
 """

import collections

# Time:  O((m + n) * k), where m is string length, n is dictionary size, k is word length
# Space: O(n * k)


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or not words[0]:
            return []

        m, n, k = len(s), len(words), len(words[0])
        if m < n * k:
            return []

        result = []
        lookup = collections.defaultdict(int)
        for word in words:
            lookup[word] += 1

        for i in range(k):
            start, end = i, i
            temp = collections.defaultdict(int)
            while end + k <= m:
                substr = s[end:end + k]
                end += k
                if substr in lookup:
                    temp[substr] += 1
                    while temp[substr] > lookup[substr]:
                        temp[s[start:start + k]] -= 1
                        start += k
                    if end - start == n * k:
                        result.append(start)

                else:
                    temp.clear()
                    start = end

        return result


if __name__ == "__main__":
    s = "wordgoodgoodgoodbestword"
    words = ['good', "good", "best", "word"]
    result = Solution().findSubstring(s, words)
    print(result)
