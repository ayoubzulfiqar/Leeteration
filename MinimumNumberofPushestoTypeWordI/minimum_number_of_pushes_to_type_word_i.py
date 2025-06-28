class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        
        total_pushes = 0
        
        letters_processed = 0
        current_cost_per_letter = 1
        num_keys = 8
        
        while letters_processed < n:
            num_letters_in_this_batch = min(num_keys, n - letters_processed)
            
            total_pushes += num_letters_in_this_batch * current_cost_per_letter
            
            letters_processed += num_letters_in_this_batch
            
            current_cost_per_letter += 1
            
        return total_pushes