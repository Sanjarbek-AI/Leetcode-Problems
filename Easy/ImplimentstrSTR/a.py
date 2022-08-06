# Implement strStr().
#
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.


def str_str(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle == "":
        return 0
    if needle in haystack:
        return haystack.find(needle)
    return -1
