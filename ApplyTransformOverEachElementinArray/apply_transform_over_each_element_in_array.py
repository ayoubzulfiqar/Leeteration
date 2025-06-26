def map_array_transform(arr, fn):
    transformed_arr = []
    for i in range(len(arr)):
        transformed_arr.append(fn(arr[i], i))
    return transformed_arr