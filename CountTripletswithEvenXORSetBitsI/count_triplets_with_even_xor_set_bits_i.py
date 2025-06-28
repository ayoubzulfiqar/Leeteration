class Solution:
    def countSetBits(self, n: int) -> int:
        return bin(n).count('1')
    
    def countTriplets(self, nums: list[int]) -> int:
        
        parities = []
        for x in nums:
            parities.append(self.countSetBits(x) % 2)
        
        count0 = parities.count(0)
        count1 = parities.count(1)
        
        total_triplets = 0
        
        # Case 1: All three chosen numbers have an even popcount parity (0, 0, 0)
        # The sum of their parities (0 + 0 + 0 = 0) is even.
        # Number of ways to choose 3 items from 'count0' items: C(count0, 3)
        if count0 >= 3:
            total_triplets += (count0 * (count0 - 1) * (count0 - 2)) // 6
            
        # Case 2: One chosen number has an even popcount parity (0) and two have odd popcount parities (1, 1)
        # The sum of their parities (0 + 1 + 1 = 2) is even.
        # Number of ways to choose 1 item from 'count0' items: C(count0, 1) = count0
        # Number of ways to choose 2 items from 'count1' items: C(count1, 2) = count1 * (count1 - 1) / 2
        if count0 >= 1 and count1 >= 2:
            total_triplets += count0 * (count1 * (count1 - 1) // 2)
            
        return total_triplets