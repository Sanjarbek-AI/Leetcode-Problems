# Given an array, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):
    nums.reverse()
    for i in range(k):
        nums.append(nums[i])
    nums[:] = nums[k:]
    nums.reverse()

    return nums
