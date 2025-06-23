class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        i = 0
        count = 0
        length = len(flowerbed)

        while i < length:
            if flowerbed[i] == 0:
                # Check if the plot to the left is empty or if it's the first plot
                left_is_empty_or_boundary = (i == 0 or flowerbed[i-1] == 0)
                
                # Check if the plot to the right is empty or if it's the last plot
                right_is_empty_or_boundary = (i == length - 1 or flowerbed[i+1] == 0)

                if left_is_empty_or_boundary and right_is_empty_or_boundary:
                    # Plant a flower by marking the plot as 1
                    flowerbed[i] = 1
                    count += 1
                    
                    # If we have planted enough flowers, we can stop
                    if count >= n:
                        return True
                    
                    # Since a flower was just planted at 'i', the next plot 'i+1' cannot have a flower.
                    # We can skip checking 'i+1' by incrementing 'i' an extra time.
                    i += 1 
            
            # Move to the next plot
            i += 1
        
        # After iterating through all plots, return true if enough flowers were planted
        return count >= n