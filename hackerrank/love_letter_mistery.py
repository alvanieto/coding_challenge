def theLoveLetterMystery(data):
    num_operations = 0
    for index in range(int(len(data) / 2)):
        num_operations += abs(ord(data[index]) - ord(data[-index - 1]))
    return num_operations
