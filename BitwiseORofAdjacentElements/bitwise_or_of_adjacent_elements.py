def bitwise_or_adjacent(arr):
    result = []
    for i in range(len(arr) - 1):
        or_value = arr[i] | arr[i+1]
        result.append(or_value)
    return result