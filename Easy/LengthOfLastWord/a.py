def length_of_last_word(s):
    s = s.strip()[::-1]
    i = 0
    for char in s:
        if char == " ":
            return i
        else:
            i += 1
    return i


print(length_of_last_word("My name is Sanjar"))
