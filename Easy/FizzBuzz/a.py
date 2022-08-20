#Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    return_list = list()
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            return_list.append("FizzBuzz")
        elif i % 3 == 0:
            return_list.append("Fizz")
        elif i % 5 == 0:
            return_list.append("Buzz")
        else:
            return_list.append(str(i))
    return return_list
