""" 179. Largest Number - Medium

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
 """


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        result = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if result[0] == "0" else result


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(nums))
