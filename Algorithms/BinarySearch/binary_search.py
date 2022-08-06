# If I explain how binary search works, it works like that: if you have a sorted list of elements and you are searching
# something in it. In simple way it started with the middle of the list and ask: is that lower then your number or
# higher. If your number is bigger then it's guess it equals the lowest number for itself it's guess and ask again
# and again. When your number and it's guess is equal it returns that number.
# Big(O): In the worth case: Log2(n) | Time complexity
# Big(O): In the best case: O(1) | Time complexity

# You can see below the example of how it works.

sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


# let's image you select one number from that list, maybe it would be: 14

# binary search function
def binary_search(numbers: list, number: int):
    low = 0
    high = len(numbers) - 1
    step = 1
    while low <= high:
        mid = (low + high) // 2
        guess = numbers[mid]
        if guess == number:
            print("Steps:", step)
            return numbers[mid]
        elif guess > number:
            high = mid - 1
        else:
            low = mid + 1
        step += 1

    return None


print(binary_search(sorted_numbers, 14))
