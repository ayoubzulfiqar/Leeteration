class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary_n = bin(n)[2:]
        complement_binary_list = ['1' if bit == '0' else '0' for bit in binary_n]
        complement_binary_str = "".join(complement_binary_list)
        return int(complement_binary_str, 2)