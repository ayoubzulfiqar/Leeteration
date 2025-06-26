def chunk(arr: list, size: int) -> list[list]:
    """
    Given an array arr and a chunk size size, return a chunked array.
    A chunked array contains the original elements in arr, but consists of subarrays each of length size.
    The length of the last subarray may be less than size if arr.length is not evenly divisible by size.
    """
    chunked_array = []
    for i in range(0, len(arr), size):
        chunked_array.append(arr[i:i + size])
    return chunked_array