class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result
        elif k > 0:
            for i in range(n):
                current_sum = 0
                for j in range(1, k + 1):
                    current_sum += code[(i + j) % n]
                result[i] = current_sum
        else:  # k < 0
            abs_k = abs(k)
            for i in range(n):
                current_sum = 0
                for j in range(1, abs_k + 1):
                    current_sum += code[(i - j + n) % n]
                result[i] = current_sum
        return result