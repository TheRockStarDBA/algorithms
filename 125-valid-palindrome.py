""" 125. Valid Palindrome - Easy
topic: string, two-pointers
related:    Palindrome Linked List - Easy
            Valid Palindrome II - Easy

Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false """


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.convert(s)
        for j in range(len(s) // 2):
            if s[j] != s[len(s) - j - 1]:
                return False

        return True

    def convert(self, s):
        ans = ""
        for i in range(len(s)):
            if s[i].isalnum():
                ans += s[i].lower()
        return ans


class Solution2(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        convertedS = [c for c in s.lower() if c.isalnum()]
        return convertedS == convertedS[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    print(Solution().isPalindrome(s))
    print(Solution2().isPalindrome(s2))