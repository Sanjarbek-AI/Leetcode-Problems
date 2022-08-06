# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def is_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    counter = dict()

    for char in s:
        if char not in counter:
            counter[char] = 1
            continue
        counter[char] += 1

    for char in t:
        if char in counter:
            counter[char] -= 1
            continue
        return False

    for val in counter.values():
        if val != 0:
            return False
    return True
