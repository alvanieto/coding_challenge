import math


def palindromeIndex(s):
    middle_down = math.ceil((len(s) - 1) / 2)
    middle_up = math.floor((len(s) - 1) / 2)
    if s == s[::-1]:
        return -1
    for index in range(len(s)):
        new_string = s[:index] + s[index + 1:]
        if new_string[:middle_down] == new_string[middle_up:][::-1]:
            return index
    return -1
