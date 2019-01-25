""" 58. Length of Last Word - Easy

Topic: string

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5 """


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])


class Solution2(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length


if __name__ == "__main__":
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution2().lengthOfLastWord("   apple   "))