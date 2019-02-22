""" 127. Word Ladder - Medium
topic: breath-first search
related:    126. Word Ladder II - Hard
            Minimum Genetic Mutation - Medium

Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a
transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation. """

#  -------------------------------
#   Breadth First Search approach
#  -------------------------------
#   For example:
#
#      start = "hit"
#      end = "cog"
#      dict = ["hot","dot","dog","lot","log","dit","hig", "dig"]
#
#                       +-----+
#         +-------------+ hit +--------------+
#         |             +--+--+              |
#         |                |                 |
#      +--v--+          +--v--+           +--v--+
#      | dit |    +-----+ hot +---+       | hig |
#      +--+--+    |     +-----+   |       +--+--+
#         |       |               |          |
#         |    +--v--+         +--v--+    +--v--+
#         +----> dot |         | lot |    | dig |
#              +--+--+         +--+--+    +--+--+
#                 |               |          |
#              +--v--+         +--v--+       |
#         +----> dog |         | log |       |
#         |    +--+--+         +--+--+       |
#         |       |               |          |
#         |       |    +--v--+    |          |
#         |       +--->| cog |<-- +          |
#         |            +-----+               |
#         |                                  |
#         |                                  |
#         +----------------------------------+
#
#      1) queue <==  "hit"
#      2) queue <==  "dit", "hot", "hig"
#      3) queue <==  "dot", "lot", "dig"
#      4) queue <==  "dog", "log"
#
#   One of the most important step here is to figure out how to find adjacent
#   nodes i.e. words which differ by one letter.
#
from string import ascii_lowercase


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        cur_level, depth = [beginWord], 0
        visited, lookup = set([beginWord]), set(wordList)
        n = len(beginWord)

        while cur_level:
            next_level = []
            for word in cur_level:
                if word == endWord:
                    return depth + 1
                for i in range(n):
                    for char in ascii_lowercase:
                        candidate = word[:i] + char + word[i + 1:]
                        if candidate not in visited and candidate in lookup:
                            visited.add(candidate)
                            next_level.append(candidate)

            depth += 1
            cur_level = next_level

        return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = Solution().ladderLength(beginWord, endWord, wordList)
    print(result)
