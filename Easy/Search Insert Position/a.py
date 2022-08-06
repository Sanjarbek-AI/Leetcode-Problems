class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for num in nums:
            if num == target:
                return nums.index(num)
            elif num > target:
                return nums.index(num)
            elif target > nums[-1]:
                return len(nums)


a = Solution()
a.searchInsert([1, 2, 3, 4, 5], 7)
