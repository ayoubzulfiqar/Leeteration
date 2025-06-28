class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        remainder_counts = [0] * 24
        count = 0

        for h in hours:
            remainder = h % 24
            
            if remainder == 0:
                count += remainder_counts[0]
            else:
                complement_remainder = 24 - remainder
                count += remainder_counts[complement_remainder]
            
            remainder_counts[remainder] += 1
            
        return count