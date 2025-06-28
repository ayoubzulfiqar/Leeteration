def solve():
    def encrypt(x: int) -> int:
        s_x = str(x)
        max_digit = '0'
        for digit_char in s_x:
            if digit_char > max_digit:
                max_digit = digit_char
        
        num_digits = len(s_x)
        
        encrypted_str = max_digit * num_digits
        return int(encrypted_str)

    # This part would typically be how the function is called
    # For a complete solution, it needs to accept input.
    # Assuming the problem implies a function that takes `nums` as an argument.

    # If this is meant to be a class method or a standalone function,
    # I'll provide the function signature.
    # Let's assume it's a function that takes `nums` directly.

    # Example usage for testing (not part of the final output, just for thought process)
    # nums1 = [1, 2, 3]
    # nums2 = [10, 21, 31]

    # For the final output, I will define the main function as requested.

    class Solution:
        def sumOfEncryptedInt(self, nums: list[int]) -> int:
            total_sum = 0
            for num in nums:
                total_sum += encrypt(num)
            return total_sum

    # The problem description implies a standalone function or a class method.
    # Given the common competitive programming format, a class with a method is typical.
    # Or a simple function. I will provide a simple function as it's more direct.

    # Let's define the function directly as `sumOfEncryptedInt`

    # To make it a complete .py solution, I will define the function and
    # assume it will be called with the input `nums`.

    # The problem statement does not provide a function signature,
    # but implies one like `sumOfEncryptedInt(nums)`.

    # Final decision: Provide a single function `sumOfEncryptedInt` that encapsulates the logic.
    # The helper `encrypt` function will be defined inside or outside.
    # Defining it inside the main function is clean if it's only used there.
    # Or as a separate helper. I'll make it a separate helper for clarity.

    return Solution() # This is a placeholder, the actual code will be the function definition.

# The actual code to be generated:

def sumOfEncryptedInt(nums: list[int]) -> int:
    def encrypt(x: int) -> int:
        s_x = str(x)
        max_digit_char = '0'
        for digit_char in s_x:
            if digit_char > max_digit_char:
                max_digit_char = digit_char
        
        num_digits = len(s_x)
        
        encrypted_str = max_digit_char * num_digits
        return int(encrypted_str)

    total_sum = 0
    for num in nums:
        total_sum += encrypt(num)
    return total_sum

