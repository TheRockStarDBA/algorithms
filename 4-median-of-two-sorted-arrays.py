""" 4. Median of Two Sorted Arrays - Hard

Topic: array, binary search, divide and conquer

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should
be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5 """


# Binary Search Approach
# Time:  O(log(min(m, n)))
# Space: O(1)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        k = (len1 + len2) // 2
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, k + 1)
        else:
            return (self.getKth(nums1, nums2, k + 1) + self.getKth(
                nums1, nums2, k)) / 2.0

    def getKth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            return self.getKth(B, A, k)

        left, right = 0, m
        while left < right:
            mid = left + (right - left) // 2
            if 0 <= k - mid - 1 < n and A[mid] >= B[k - mid - 1]:
                right = mid
            else:
                left = mid + 1

        Ai = A[left - 1] if left - 1 >= 0 else float("-inf")
        Bj = B[k - 1 - left] if k - 1 - left >= 0 else float("-inf")

        return max(Ai, Bj)


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 2], [1, 2, 3]))
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
