#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
#Example 1:
#
#Input: 121
#Output: true
#Example 2:
#
#Input: -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#Example 3:
#
#Input: 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#Follow up:
#
#Coud you solve it without converting the integer to a string?

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        s=str(x)
        n=len(s)
        if n == 1:
            return True
        else:
            i,j = 0, n-1
            while i<j:
                if s[i]!=s[j]:
                    return False
            
                i+=1
                j-=1
            return True

    def isPalindrome2(self, x):
        if x < 0 :
            return False
        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while ranger > 1:
            left, x =divmod(x, ranger)
            x, right = divmod(x, 10)
            if left != right:
                return False
            ranger //= 100

        return True