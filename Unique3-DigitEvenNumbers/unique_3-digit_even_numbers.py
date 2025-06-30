import collections

class Solution:
    def countEvenNumbers(self, digits: list[int]) -> int:
        available_counts = collections.Counter(digits)
        
        valid_numbers = set()
        
        for num in range(100, 1000):
            if num % 2 != 0:
                continue
            
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            current_num_digits = [d1, d2, d3]
            current_num_counts = collections.Counter(current_num_digits)
            
            can_form = True
            for digit, count in current_num_counts.items():
                if available_counts[digit] < count:
                    can_form = False
                    break
            
            if can_form:
                valid_numbers.add(num)
                
        return len(valid_numbers)