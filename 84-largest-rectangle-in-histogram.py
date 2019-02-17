""" 84. Largest Rectangle in Histogram - Hard
topic: array, stack
related:  Maximal Rectangle - Hard

Given n non-negative integers representing the histogram's bar height where the
width of each bar is 1, find the area of largest rectangle in the histogram.

 *                    6
 *                  +---+
 *               5  |   |
 *              +---+   |
 *              |   |   |
 *              |   |   |
 *              |   |   |     3
 *              |   |   |   +---+
 *        2     |   |   | 2 |   |
 *      +---+   |   |   +---+   |
 *      |   | 1 |   |   |   |   |
 *      |   +---+   |   |   |   |
 *      |   |   |   |   |   |   |
 *      +---+---+---+---+---+---+

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 *                    6
 *                  +---+
 *               5  |   |
 *              +-------|
 *              |-------|
 *              |-------|
 *              |-------|     3
 *              |-------|   +---+
 *        2     |-------| 2 |   |
 *      +---+   |-------|---+   |
 *      |   | 1 |-------|   |   |
 *      |   +---|-------|   |   |
 *      |   |   |-------|   |   |
 *      +---+---+---+---+---+---+

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
 """


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxArea = 0
        heights.append(0)
        i = 0
        while i < len(heights):
            if not stack or (heights[i] >= heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                topIdx = stack.pop()
                if not stack:
                    maxArea = max(maxArea, heights[topIdx] * i)
                else:
                    maxArea = max(maxArea,
                                  heights[topIdx] * (i - stack[-1] - 1))

        return maxArea


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    area = Solution().largestRectangleArea(heights)
    print(area)