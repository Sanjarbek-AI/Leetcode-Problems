def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    a = x // 2
    for num in range(1, a):
        if num * num == x:
            return num


print(mySqrt(8))
