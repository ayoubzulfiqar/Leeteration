def filterElements(arr, fn):
    filteredArr = []
    for i in range(len(arr)):
        try:
            if bool(fn(arr[i], i)):
                filteredArr.append(arr[i])
        except TypeError:
            if bool(fn(arr[i])):
                filteredArr.append(arr[i])
    return filteredArr