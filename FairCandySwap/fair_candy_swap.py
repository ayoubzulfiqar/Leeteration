class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)

        # Let x be the candy Alice gives and y be the candy Bob gives.
        # After exchange:
        # Alice's new total: sumA - x + y
        # Bob's new total: sumB - y + x
        # For them to be equal:
        # sumA - x + y = sumB - y + x
        # Rearranging the equation:
        # sumA - sumB = 2x - 2y
        # sumA - sumB = 2 * (x - y)
        # (sumA - sumB) / 2 = x - y
        # So, y = x - (sumA - sumB) / 2

        # Calculate the required difference 'delta'
        # If Alice gives x and gets y, her sum changes by (y - x).
        # If Bob gives y and gets x, his sum changes by (x - y).
        # We need sumA + (y - x) = sumB + (x - y)
        # sumA - sumB = (x - y) + (x - y)
        # sumA - sumB = 2 * (x - y)
        # (sumA - sumB) // 2 = x - y
        # Let diff = (sumA - sumB) // 2
        # Then, y = x - diff

        diff = (sumA - sumB) // 2

        # Convert bobSizes to a set for efficient lookups
        bob_candies_set = set(bobSizes)

        # Iterate through Alice's candies
        for x in aliceSizes:
            # Calculate the required candy 'y' that Bob must have
            y_required = x - diff
            # Check if this 'y_required' exists in Bob's candies
            if y_required in bob_candies_set:
                return [x, y_required]

        # The problem guarantees that at least one answer exists,
        # so this line should theoretically not be reached.
        return []