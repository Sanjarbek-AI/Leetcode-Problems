def longest_common_prefix(strs):
    result = ""
    i = 0

    while i < len(strs[0]):
        for string in strs:
            if i >= len(string):
                return result
            if string[i] != strs[0][i]:
                return result

        result += strs[0][i]
        i += 1

    return result


print(longest_common_prefix(["flower", "flow", "flight"]))
