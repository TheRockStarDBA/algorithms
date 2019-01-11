#11. Container With Most Water
#TOPIC: ARRAY; TWO-POINTERS (Medium)
#Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
#n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
#Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
#Note: You may not slant the container and n is at least 2.
#Example:
#
#Input: [1,8,6,2,5,4,8,3,7]
#Output: 49

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i,j = 0, len(height)-1

        while i<j:
            if height[i]>height[j]:
                area = (j-i)*height[j]
                res = max(area, res)
                j-=1

            else:
                area = (j-i)*height[i]
                res = max(area, res)
                i+=1

        return res

if __name__ == "__main__":
    assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
