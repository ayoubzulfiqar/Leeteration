class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        current_sum = 0

        # Prioritize picking items with '1'
        # Pick as many '1's as possible, up to k or numOnes
        if k > 0:
            count_to_pick = min(k, numOnes)
            current_sum += count_to_pick * 1
            k -= count_to_pick

        # If k items are still needed, pick items with '0'
        # Pick as many '0's as possible, up to remaining k or numZeros
        if k > 0:
            count_to_pick = min(k, numZeros)
            current_sum += count_to_pick * 0  # Adding 0 does not change sum, but consumes k
            k -= count_to_pick

        # If k items are still needed, pick items with '-1'
        # Pick as many '-1's as possible, up to remaining k or numNegOnes
        if k > 0:
            count_to_pick = min(k, numNegOnes)
            current_sum += count_to_pick * (-1)
            k -= count_to_pick
        
        return current_sum