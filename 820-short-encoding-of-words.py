""" 820. Short Encoding of Words - Medium

Given a list of words, we may encode it by writing a reference string S and a
list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as
S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference
string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the
given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].

Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters. """

import collections
import functools


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = list(set(words))
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        nodes = [
            functools.reduce(dict.__getitem__, word[::-1], trie)
            for word in words
        ]

        return sum(
            len(word) + 1 for i, word in enumerate(words)
            if len(nodes[i]) == 0)


if __name__ == "__main__":
    words = ["time", "me", "bell"]
    res = Solution().minimumLengthEncoding(words=words)
    #print(res)