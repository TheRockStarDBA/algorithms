#Given an array of strings, group anagrams together.
#
#Example:
#
#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]
#Note:
#
#All inputs will be in lowercase.
#The order of your output does not matter.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = []
        mapping = {}
        for s in strs:
            root = ''.join(sorted(s))
            if root not in mapping:
                mapping[root]=[s]
            else:
                mapping[root].append(s)

        [res.append(v) for k,v in mapping.items()]

        return res



        


test_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Solution().groupAnagrams(test_strs)