# Selection sort is one of the most popular sorting algorithm in the world. It works like that:
# Imagine you have list of number which are not ordered you just need to sort them.
# with selection sort you just need to open new list and find the smallest element or biggest element in
# unsorted list. When you find it you add it to new list and remove it from unsorted list. That how it works.
# Big(O): In the worth case: O(n**2) | Time complexity

def find_smallest(nums: list):
    smallest_num = nums[0]
    smallest_index = 0

    for i in range(1, len(nums)):
        if nums[i] < smallest_num:
            smallest_num = nums[i]
            smallest_index = i
    return smallest_index


def selection_sort(nums: list):
    new_list = list()
    for _ in range(len(nums)):
        smallest = find_smallest(nums)
        new_list.append(nums.pop(smallest))
    return new_list


print(selection_sort([2, 1, 5, 3, 2, 4, 6]))
