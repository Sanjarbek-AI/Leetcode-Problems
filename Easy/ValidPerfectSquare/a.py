# Given a positive integer num, write a function which returns True if num is a perfect square
# else False. Follow up: Do not use any built-in library function such as sqrt.


def is_perfect_square(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 1:
        return True
    low = 1
    high = num // 2

    while low <= high:
        mid = (low + high) // 2

        if mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            high = mid - 1
        else:
            low = mid + 1
    return False
