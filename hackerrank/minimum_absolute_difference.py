def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = arr[1] - arr[0]
    for i in range(len(arr) - 1):
        abs_diff = arr[i + 1] - arr[i]
        if abs_diff < min_diff:
            min_diff = abs_diff
    return min_diff
