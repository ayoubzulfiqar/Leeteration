def find_upper_bound(arr, target):
    """
    Finds the index of the first element in a sorted array that is strictly greater than the target value.
    If no such element exists, returns the length of the array.
    This is equivalent to std::upper_bound in C++.

    Args:
        arr (list): A sorted list of numbers.
        target (int/float): The value to search for.

    Returns:
        int: The index of the first element strictly greater than the target,
             or len(arr) if all elements are less than or equal to the target.
    """
    low = 0
    high = len(arr)
    ans = len(arr)

    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > target:
            ans = mid
            high = mid
        else:
            low = mid + 1
    return ans

if __name__ == '__main__':
    # Example Usage:
    # Test Case 1: Standard case with duplicates
    arr1 = [1, 2, 2, 3, 4]
    target1 = 2
    # Expected: Index of 3, which is 3
    # print(f"Array: {arr1}, Target: {target1}, Upper Bound Index: {find_upper_bound(arr1, target1)}")

    # Test Case 2: Target is smaller than all elements
    arr2 = [10, 20, 30, 40]
    target2 = 5
    # Expected: Index of 10, which is 0
    # print(f"Array: {arr2}, Target: {target2}, Upper Bound Index: {find_upper_bound(arr2, target2)}")

    # Test Case 3: Target is larger than all elements
    arr3 = [1, 2, 3, 4]
    target3 = 5
    # Expected: len(arr3), which is 4
    # print(f"Array: {arr3}, Target: {target3}, Upper Bound Index: {find_upper_bound(arr3, target3)}")

    # Test Case 4: Target is equal to the last element
    arr4 = [1, 2, 3, 4]
    target4 = 4
    # Expected: len(arr4), which is 4
    # print(f"Array: {arr4}, Target: {target4}, Upper Bound Index: {find_upper_bound(arr4, target4)}")

    # Test Case 5: Empty array
    arr5 = []
    target5 = 10
    # Expected: 0
    # print(f"Array: {arr5}, Target: {target5}, Upper Bound Index: {find_upper_bound(arr5, target5)}")

    # Test Case 6: Single element array, target less than
    arr6 = [5]
    target6 = 3
    # Expected: 0
    # print(f"Array: {arr6}, Target: {target6}, Upper Bound Index: {find_upper_bound(arr6, target6)}")

    # Test Case 7: Single element array, target equal
    arr7 = [5]
    target7 = 5
    # Expected: 1
    # print(f"Array: {arr7}, Target: {target7}, Upper Bound Index: {find_upper_bound(arr7, target7)}")

    # Test Case 8: Single element array, target greater
    arr8 = [5]
    target8 = 7
    # Expected: 1
    # print(f"Array: {arr8}, Target: {target8}, Upper Bound Index: {find_upper_bound(arr8, target8)}")

    # Test Case 9: All elements are the same
    arr9 = [7, 7, 7, 7]
    target9 = 7
    # Expected: 4
    # print(f"Array: {arr9}, Target: {target9}, Upper Bound Index: {find_upper_bound(arr9, target9)}")

    # Test Case 10: Negative numbers
    arr10 = [-5, -2, 0, 3, 8]
    target10 = -2
    # Expected: Index of 0, which is 2
    # print(f"Array: {arr10}, Target: {target10}, Upper Bound Index: {find_upper_bound(arr10, target10)}")