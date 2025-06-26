class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        
        idx_1 = -1
        idx_n = -1
        
        for i in range(n):
            if nums[i] == 1:
                idx_1 = i
            if nums[i] == n:
                idx_n = i
        
        # Calculate the number of swaps to move 1 to the first position (index 0).
        # This is simply its current index.
        swaps_for_1 = idx_1
        
        # Calculate the number of swaps to move n to the last position (index n-1).
        # This is the distance from its current position to the end.
        # We need to consider if the movement of 1 affects n's position.
        
        if idx_1 < idx_n:
            # If 1 is to the left of n, moving 1 to the front (left) does not affect
            # n's relative position with respect to the end of the array.
            # n needs to move (n-1 - idx_n) positions to the right.
            swaps_for_n = (n - 1) - idx_n
        else: # idx_1 > idx_n
            # If 1 is to the right of n, when 1 moves to the front (left),
            # it will swap past n. Each time 1 swaps with an element to its left,
            # that element effectively shifts one position to the right.
            # So, n will be shifted one position to the right.
            # Its effective new index will be idx_n + 1.
            # Therefore, n needs to move (n-1 - (idx_n + 1)) positions to the right.
            swaps_for_n = (n - 1) - (idx_n + 1)
            
        return swaps_for_1 + swaps_for_n