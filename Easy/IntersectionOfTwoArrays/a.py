# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the
# result must appear as many times as it shows in both arrays and you may return the result in any order.


def intersect(nums1, nums2):
    new_list = list()
    if len(nums1) > len(nums2):
        for num in nums2:
            if num in nums1:
                nums1.remove(num)
                new_list.append(num)
    else:
        for num in nums1:
            if num in nums2:
                nums2.remove(num)
                new_list.append(num)
    return new_list
