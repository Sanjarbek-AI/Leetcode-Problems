# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def single_number(nums):
    nums.sort()
    i = 0
    while i < len(nums):
        if i == len(nums) - 1 or nums[i] != nums[i + 1]:
            return nums[i]
        i += 2
