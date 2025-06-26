import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        # The sum of all elements between 1 and x inclusively is S_left = x * (x + 1) / 2
        # The sum of all elements between x and n inclusively is S_right.
        # S_right can be calculated as the total sum from 1 to n minus the sum from 1 to x-1.
        # Total sum S_n = n * (n + 1) / 2
        # Sum from 1 to x-1 is S_x_minus_1 = (x - 1) * x / 2
        # So, S_right = S_n - S_x_minus_1
        # S_right = n * (n + 1) / 2 - (x - 1) * x / 2

        # For x to be the pivot integer, S_left must equal S_right:
        # x * (x + 1) / 2 = n * (n + 1) / 2 - (x - 1) * x / 2

        # Multiply the entire equation by 2 to clear denominators:
        # x * (x + 1) = n * (n + 1) - (x - 1) * x
        # x^2 + x = n^2 + n - (x^2 - x)
        # x^2 + x = n^2 + n - x^2 + x

        # Subtract 'x' from both sides:
        # x^2 = n^2 + n - x^2

        # Add 'x^2' to both sides:
        # 2 * x^2 = n^2 + n
        # 2 * x^2 = n * (n + 1)

        # Solve for x^2:
        # x^2 = n * (n + 1) / 2

        # For x to be an integer, n * (n + 1) / 2 must be a perfect square.
        # Calculate the value that x^2 should be:
        val_for_x_squared = n * (n + 1) // 2

        # Calculate the integer square root of this value.
        # We use math.sqrt and then convert to int.
        # If the number is a perfect square, int(sqrt(num)) will be the correct integer root.
        # Otherwise, it will be floor(sqrt(num)).
        x_candidate = int(math.sqrt(val_for_x_squared))

        # Check if the calculated x_candidate, when squared, equals the original value.
        # This confirms if val_for_x_squared was indeed a perfect square.
        if x_candidate * x_candidate == val_for_x_squared:
            # Additionally, ensure x_candidate is within the valid range [1, n].
            # From the derivation x^2 = n*(n+1)/2, it can be shown that x <= n for n >= 1.
            # And x >= 1 is also true for n >= 1.
            # So, if it's a perfect square, x_candidate will be a valid pivot.
            return x_candidate
        else:
            # If val_for_x_squared is not a perfect square, no integer x exists.
            return -1