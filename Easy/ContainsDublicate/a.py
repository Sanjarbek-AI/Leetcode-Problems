# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

def contains_duplicate(nums: list):
    set_nums_len = len(set(nums))
    nums_len = len(nums)
    return nums_len > set_nums_len
