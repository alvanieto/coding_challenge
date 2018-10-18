def hourglassSum(arr):
    max_ = None
    for x in range(4):
        for y in range(4):
            sum_ = sum(_extract_hourglass(arr, x, y))
            if max_ is None or sum_ > max_:
                max_ = sum_
    return max_


def _extract_hourglass(arr, x, y):
    hourglass = arr[x][y:y+3]               # a b c
    hourglass.append(arr[x+1][y+1])         #   d
    hourglass.extend(arr[x+2][y:y+3])       # e f g
    return hourglass
