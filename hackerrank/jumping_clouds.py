def jumpingOnClouds(c):
    return sum(generator(c))


def generator(c):
    index = 0
    size = len(c)
    while index < size - 1:
        index += 2 if index + 2 < size and c[index + 2] == 0 else 1
        yield 1
