class Solution:
    def solve(self, s: str) -> str:
        n = len(s)
        s_list = list(s)

        for i in range(n - 1):
            digit1 = int(s_list[i])
            digit2 = int(s_list[i+1])

            # Check if digits have the same parity
            if (digit1 % 2) == (digit2 % 2):
                # Check if swapping them results in a lexicographically smaller string
                if digit2 < digit1:
                    # Perform the swap
                    s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
                    # Return immediately as we found the first optimal swap from left to right
                    return "".join(s_list)

        # If no suitable swap was found, the original string is already the lexicographically smallest
        return "".join(s_list)