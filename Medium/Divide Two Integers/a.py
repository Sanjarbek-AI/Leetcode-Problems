def divide(dividend, divisor):
    i = 0
    last = 1
    if dividend < 0 and divisor < 0:
        dividend *= -1
        divisor *= -1
    elif dividend > 0 and divisor < 0:
        last = -1
        divisor *= -1
    elif dividend < 0 and divisor > 0:
        last = -1
        dividend *= -1

    while dividend >= divisor:
        i += 1
        dividend -= divisor

    return i * last


print(divide(41, -3))
