import collections

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq_map = collections.Counter(nums)
        
        good_pairs_count = 0
        
        for count in freq_map.values():
            if count >= 2:
                good_pairs_count += (count * (count - 1)) // 2
                
        return good_pairs_count