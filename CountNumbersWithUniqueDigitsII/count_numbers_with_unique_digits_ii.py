class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        ans = 10  # For n=1, numbers 0-9 have unique digits.
        
        # current_unique_count tracks the count of unique-digit numbers for the current length (k digits).
        # For k=1, numbers 1-9 (9 numbers).
        # For k=2, numbers like 10-99 with unique digits.
        current_unique_count = 9 
        
        # available_choices tracks the number of distinct digits available for the next position.
        # For the first digit (1-9), 9 choices.
        # For the second digit, 9 choices (0-9 excluding the first).
        # For the third digit, 8 choices (0-9 excluding the first two).
        available_choices = 9 

        # Iterate from length k=2 up to n.
        for i in range(2, n + 1):
            # If we've run out of unique digits (e.g., trying to form an 11-digit number), break.
            if available_choices == 0:
                break
            
            # Calculate unique-digit numbers for the current length 'i'.
            # This is previous_count_for_length_k_minus_1 * available_choices.
            current_unique_count = current_unique_count * available_choices
            ans += current_unique_count
            
            # Decrease available choices for the next digit position.
            available_choices -= 1
                
        return ans