def sockMerchant(n, ar):
    pairs = {}
    for color in ar:
        if color not in pairs:
            pairs[color] = 0
        pairs[color] += 1
    res = 0
    for value in pairs.values():
        if value >= 2:
            res += int(value / 2)
    return res

data = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(0, data))
