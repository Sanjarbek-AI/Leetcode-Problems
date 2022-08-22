# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.


def isPowerOfFour(n):
    """
    :type n: int
    :rtype: bool
    """
    result = 1
    if n == 1:
        return True
    for i in range(1, 100):
        if result == n:
            return True
        elif result > n:
            return False
        else:
            result *= 4
