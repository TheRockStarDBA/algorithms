""" 6. Longest Palindromic Substring
Topics: array, dynamic programming (Medium)

Related: Shortest Palindrome (Hard)
Palindrome Permutation (Easy)
Palindrome Pairs (Hard)
Longest Palindromic Subsequence (Medium)
Palindromic Substrings (Medium)

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb" """

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
        	return ""
        maxLen=1
        start=0
        for i in xrange(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]

if __name__ =='__main__':
    result = Solution().longestPalindrome("babad")
    print(result)