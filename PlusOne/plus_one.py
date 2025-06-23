class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        # If we reach here, it means all digits were 9s (e.g., [9,9,9])
        # We need to prepend a 1 and the rest will be zeros.
        return [1] + digits