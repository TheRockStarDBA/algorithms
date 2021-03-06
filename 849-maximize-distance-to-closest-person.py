""" 849. Maximize Distance to Closest Person - Easy
##array

In a row of seats, 1 represents a person sitting in that seat, and 0 represents
that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest
person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
 """

# Two pointers
# Time:  O(n)
# Space: O(1)


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        occupied = (idx for idx, seat in enumerate(seats) if seat)
        prev, future = None, next(occupied)
        ans = 0
        for idx, seat in enumerate(seats):
            if seat:
                prev = idx
            else:
                while future is not None and future < idx:
                    future = next(occupied, None)
            left = float('inf') if prev is None else idx - prev
            right = float('inf') if future is None else future - idx
            ans = max(ans, min(left, right))
        return ans


class Solution2(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        prev, ans = -1, 1
        for i, seat in enumerate(seats):
            if seat:
                if prev < 0:
                    ans = i
                else:
                    ans = max(ans, (i - prev) // 2)
                prev = i
        return max(ans, len(seats) - 1 - prev)


if __name__ == "__main__":
    ans = Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1])
    print(ans)