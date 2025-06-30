import collections

class Solution:
    def minDeletions(self, s: str, k: int) -> int:
        char_counts = collections.Counter(s)
        frequencies = list(char_counts.values())
        frequencies.sort()
        
        distinct_chars = len(frequencies)
        
        if distinct_chars <= k:
            return 0
            
        deletions = 0
        num_to_remove = distinct_chars - k
        
        for i in range(num_to_remove):
            deletions += frequencies[i]
            
        return deletions