class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        result = []

        while start < end:
            mid = start + int((end - start) / 2)
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                result.append(mid)
                break
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        if not result:
            return [-1, -1]

        end = len(nums) - 1

        while start < end:
            mid = start + int((end - start) / 2)
            if nums[mid] == target and (mid == len(nums) - 1
                                        or nums[mid + 1] != target):
                result.append(mid)
                break
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        return result


if __name__ == "__main__":
    solution = Solution()
    result = solution.searchRange([5, 7, 7, 8, 8, 10], 8)
    print(result)