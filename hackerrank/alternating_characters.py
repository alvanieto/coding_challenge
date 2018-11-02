def alternatingCharacters(s):
    prev_char = ''
    count = 0
    for char_ in s:
        if prev_char and prev_char == char_:
            count += 1
        prev_char = char_
    return count
