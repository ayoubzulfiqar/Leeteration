import collections

class Solution:
    def maxDifferenceEvenOddFrequency(self, s: str) -> int:
        freq_map = collections.Counter(s)
        
        odd_freqs = []
        even_freqs = []
        
        for freq in freq_map.values():
            if freq % 2 == 0:
                even_freqs.append(freq)
            else:
                odd_freqs.append(freq)
                
        max_odd = max(odd_freqs)
        min_even = min(even_freqs)
        
        return max_odd - min_even