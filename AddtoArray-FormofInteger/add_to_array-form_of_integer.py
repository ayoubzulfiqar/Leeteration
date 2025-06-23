class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        # Convert the array-form number 'num' into an integer.
        # This leverages Python's arbitrary-precision integers,
        # which can handle numbers with up to 10^4 digits.
        num_val = 0
        for digit in num:
            num_val = num_val * 10 + digit

        # Add the integer 'k' to the converted number.
        total_sum = num_val + k

        # Convert the resulting sum back into its array-form (list of digits).
        # Handle the special case where the sum is 0.
        if total_sum == 0:
            return [0]

        result = []
        # Extract digits from the sum one by one, from right to left.
        # This naturally adds them to the list in reverse order.
        while total_sum > 0:
            result.append(total_sum % 10)
            total_sum //= 10
        
        # Reverse the list to get the digits in left-to-right order.
        return result[::-1]