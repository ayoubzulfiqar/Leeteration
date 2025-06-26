class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True

        n = len(nums)
        max_prime = 0
        
        diagonal_elements = set()

        for i in range(n):
            diagonal_elements.add(nums[i][i])
            diagonal_elements.add(nums[i][n - 1 - i])
        
        for val in diagonal_elements:
            if is_prime(val):
                if val > max_prime:
                    max_prime = val
                    
        return max_prime