def countSwaps(a):
    swaps = 0
    len_a = len(a)
    for i in range(len_a):
        for j in range(len_a - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return swaps, a


def _format_result(swaps, a):
    result = [
        'Array is sorted in {} swaps.'.format(swaps),
        'First Element: {}'.format(a[0]),
        'Last Element: {}'.format(a[-1])
    ]
    return '\n'.join(result)
