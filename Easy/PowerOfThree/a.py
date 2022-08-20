# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

def isPowerOfThree(n):
    return n > 0 and 1162261467 % n == 0

# why I solve like that the reason is that the biggest number in 32 bit which can be power of 3 is 1162261467
# if it is divide by three with no residual number n can be power of three
