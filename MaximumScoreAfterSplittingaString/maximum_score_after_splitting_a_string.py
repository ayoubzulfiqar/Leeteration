class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        
        # Initialize counts for the first possible split.
        # Initially, all '1's are considered to be in the right part,
        # and no '0's are yet in the left part.
        num_zeros_left = 0
        num_ones_right = s.count('1')
        
        # Initialize max_score to a value that will be easily surpassed.
        # Since the minimum possible score is 1 (e.g., for "00", "11", "01", "10"),
        # 0 is a safe initial value.
        max_score = 0 
        
        # Iterate through all possible split points.
        # The loop variable 'i' represents the index of the character that is
        # being moved from the 'right' part to the 'left' part.
        # The split occurs AFTER s[i].
        # So, the left substring is s[0...i] and the right substring is s[i+1...n-1].
        # 'i' goes from 0 to n-2 (inclusive) to ensure both substrings are non-empty.
        for i in range(n - 1):
            if s[i] == '0':
                num_zeros_left += 1
            else: # s[i] == '1'
                num_ones_right -= 1
            
            # Calculate the score for the current split
            current_score = num_zeros_left + num_ones_right
            
            # Update the maximum score found so far
            max_score = max(max_score, current_score)
            
        return max_score