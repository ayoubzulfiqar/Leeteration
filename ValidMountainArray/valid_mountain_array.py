class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        
        if n < 3:
            return False
        
        i = 0
        
        # Ascend the mountain (find the peak)
        # Loop while we are not at the end and the current element is strictly less than the next
        while i + 1 < n and arr[i] < arr[i+1]:
            i += 1
            
        # Check if a peak was found (not at the beginning and not at the end)
        # If i is 0, it means the array did not strictly increase at all (e.g., [3,2,1])
        # If i is n-1, it means the array only strictly increased and never decreased (e.g., [1,2,3])
        if i == 0 or i == n - 1:
            return False
            
        # Descend the mountain
        # Loop while we are not at the end and the current element is strictly greater than the next
        while i + 1 < n and arr[i] > arr[i+1]:
            i += 1
            
        # If we successfully reached the end of the array, it's a valid mountain
        return i == n - 1