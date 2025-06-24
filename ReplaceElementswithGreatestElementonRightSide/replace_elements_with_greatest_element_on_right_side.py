class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        
        # Initialize max_so_far with -1, which is the value for the last element
        # and also acts as the initial "greatest element to the right" for the
        # second to last element.
        max_so_far = -1
        
        # Iterate from the second to last element backwards to the first
        # The loop range goes from n-1 down to 0 (inclusive)
        for i in range(n - 1, -1, -1):
            # Store the current element's value before it's replaced
            # This is the 'original' value of arr[i]
            current_val = arr[i]
            
            # Replace the current element with the greatest element found so far to its right.
            # At this point, max_so_far holds the maximum of elements arr[i+1]...arr[n-1].
            arr[i] = max_so_far
            
            # Update max_so_far to be the maximum of its current value (which was the max to the right of current_val)
            # and the original value of the element we just processed (current_val).
            # This updated max_so_far will be used for the element to the left of the current one (i-1).
            max_so_far = max(max_so_far, current_val)
            
        return arr