class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [0] * n

        prev_c_idx = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev_c_idx = i
            answer[i] = i - prev_c_idx

        next_c_idx = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                next_c_idx = i
            answer[i] = min(answer[i], next_c_idx - i)
            
        return answer