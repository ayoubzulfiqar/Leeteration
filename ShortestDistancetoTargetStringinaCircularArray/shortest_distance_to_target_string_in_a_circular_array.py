class Solution:
    def shortestDistance(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        
        target_exists = False
        for word in words:
            if word == target:
                target_exists = True
                break
        
        if not target_exists:
            return -1
            
        min_dist = float('inf')
        
        for i in range(n):
            if words[i] == target:
                abs_diff = abs(i - startIndex)
                
                current_dist = min(abs_diff, n - abs_diff)
                
                min_dist = min(min_dist, current_dist)
                
        return min_dist