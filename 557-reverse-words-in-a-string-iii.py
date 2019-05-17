""" 557. Reverse Words in a String III - Easy
##string

Given a string, you need to reverse the order of characters in each word within
a sentence while still preserving whitespace and initial word order.

Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not
be any extra space in the string. """


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed = [word[::-1] for word in s.split(' ')]
        return ' '.join(reversed)


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))