class Solution:
    def similarPairs(self, words: list[str]) -> int:
        
        canonical_counts = {}
        
        for word in words:
            char_set = frozenset(word)
            canonical_counts[char_set] = canonical_counts.get(char_set, 0) + 1
            
        pair_count = 0
        for count in canonical_counts.values():
            if count >= 2:
                pair_count += count * (count - 1) // 2
                
        return pair_count