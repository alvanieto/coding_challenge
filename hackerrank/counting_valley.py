def countingValleys(n, s):
    current_level = 0
    num_valley = 0
    for char in s:
        previous_level = current_level
        current_level += 1 if char == 'U' else -1
        if previous_level == -1 and current_level == 0:
            num_valley += 1
    return num_valley
