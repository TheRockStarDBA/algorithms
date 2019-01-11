###################
#Problem
#Given a list of distinct numbers, return all possible permutations.
#
#Example
#For nums = [1,2,3], the permutations are:
#
#[
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
#]
# assume there is no repetation numbers
###################

class Solution(object):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def permute(self, nums):
        res = []
        if len(nums)==0:
            return res
        
        self.get_permute(nums, res, [])
        return res
    
    def get_permute(self, nums, res, current):
        if not nums:
            res.append(current+[])
            return
        
        for i in range(len(nums)):
  
            current.append(nums[i])
            self.get_permute(nums[:i]+nums[i+1:], res, current)
            current.pop()

if __name__ == "__main__":
    Solution().permute([1,2,3])