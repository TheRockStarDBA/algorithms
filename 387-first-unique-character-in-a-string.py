""" 387. First Unique Character in a String - Easy
##hash table ##string

Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

 """

import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        index = 0
        for char in s:
            if count[char] == 1:
                return index
            else:
                index += 1
        return -1


class Solution2(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = collections.defaultdict(int)
        candidtates = set()
        for i, char in enumerate(s):
            if lookup[char]:
                candidtates.discard(lookup[char])
            else:
                lookup[char] = i + 1
                candidtates.add(i + 1)

        return min(candidtates) - 1 if candidtates else -1


if __name__ == "__main__":
    print(Solution().firstUniqChar(s="leetcode"))
    print(Solution2().firstUniqChar(s="loveleetcode"))
