def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = abs(arr[0] - arr[1])
    for i in range(len(arr) - 1):
        abs_diff = abs(arr[i] - arr[i + 1])
        if abs_diff < min_diff:
            min_diff = abs_diff
            if min_diff == 0:
                break
    return min_diff
