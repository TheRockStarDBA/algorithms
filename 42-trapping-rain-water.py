""" 42. Trapping Rain Water - Hard
Topics: array, two-pointers, stack
Related: 11. Container With Most Water - Medium
        238. Product of Array Except Self - Medium
        407. Trapping Rain Water II - Hard
        755. Pour Water - Medium

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6 """

# Approach: Using stacks
# Intuition
# we can use stack to keep track of the bars that are bounded by longer bars and
# hence, may store water. Using the stack, we can do the calculations in only
# one iteration.
# Time:  O(n)
# Space: O(n)


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        stack = []

        for i in range(len(height)):
            mid_height = 0
            while stack:
                [pop, pop_height] = stack.pop()
                distance = i - pop - 1
                bounded_height = min(height[i], pop_height) - mid_height
                ans += distance * bounded_height
                mid_height = pop_height

                if height[i] < pop_height:
                    stack.append([pop, pop_height])
                    break

            stack.append([i, height[i]])
        return ans


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ans = Solution().trap(height)
    print(ans)