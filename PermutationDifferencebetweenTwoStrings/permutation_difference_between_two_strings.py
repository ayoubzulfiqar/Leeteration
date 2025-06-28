class Solution:
    def permutationDifference(self, s: str, t: str) -> int:
        t_indices = {}
        for i in range(len(t)):
            t_indices[t[i]] = i

        total_difference = 0
        for i in range(len(s)):
            char_s = s[i]
            index_s = i
            index_t = t_indices[char_s]
            total_difference += abs(index_s - index_t)

        return total_difference