""" 136. Single Number - Easy
**classical interview question**
topic: hash table, bit manipulation

Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4 """

# the same number XOR together will be 0. XOR all of numbers, the result is the
# number which only appears once.


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for n in nums:
            ans ^= n
        return ans


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 1]))
    print(Solution().singleNumber([4, 1, 2, 1, 2]))
