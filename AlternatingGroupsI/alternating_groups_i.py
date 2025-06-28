class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        n = len(colors)
        count = 0
        for i in range(n):
            left_idx = (i - 1 + n) % n
            right_idx = (i + 1) % n
            
            if colors[left_idx] != colors[i] and colors[i] != colors[right_idx]:
                count += 1
        return count