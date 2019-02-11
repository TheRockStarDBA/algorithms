""" 57. Insert Interval - Hard

Related:
Merge Intervals - Medium
Range Module - Hard

Given a set of non-overlapping intervals, insert a new interval into the intervals 
(merge if necessary).

You may assume that the intervals were initially sorted according to their start 
times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10]. """

# Approach :

# Let the new interval to be inserted is : [a, b]

# Case 1 : b < (starting time of first interval in set)
# In this case simply insert new interval at the beginning of the set.

# Case 2 : (ending value of last interval in set) < a
# In this case simply insert new interval at the end of the set.

# Case 3 : a ≤ (starting value of first interval) and b ≥ (ending value of last
# interval)
# In this case the new interval overlaps with all the intervals, i.e., it contains
# all the intervals. So the final answer
# is the new interval itself.

# Case 4 : The new interval does not overlap with any interval in the set and falls
# between any two intervals in the set

# Case 5 : The new interval overlaps with the interval(s) of the set.


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    # To print the result
    def __str__(self):
        return "[" + str(self.start) + "," + str(self.end) + "]"


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = newInterval.start
        end = newInterval.end
        result = []
        i = 0
        while i < len(intervals) and intervals[i].end < start:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i].start <= end:
            start = min(start, intervals[i].start)
            end = max(end, intervals[i].end)
            i += 1

        result += [Interval(start, end)]
        result += intervals[i:]

        return result


if __name__ == "__main__":
    intervals = [
        Interval(1, 2),
        Interval(3, 5),
        Interval(6, 7),
        Interval(8, 10),
        Interval(12, 16)
    ]
    newInterval = Interval(4, 8)

    intervals = Solution().insert(intervals, newInterval)

    for interval in intervals:
        print(interval)
