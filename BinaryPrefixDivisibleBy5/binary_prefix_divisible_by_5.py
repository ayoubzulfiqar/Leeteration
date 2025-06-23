class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        answer = []
        current_num_mod_5 = 0
        for bit in nums:
            current_num_mod_5 = (current_num_mod_5 * 2 + bit) % 5
            answer.append(current_num_mod_5 == 0)
        return answer