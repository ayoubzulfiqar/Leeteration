class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        answer = []
        for num in nums:
            s_num = str(num)
            for char_digit in s_num:
                answer.append(int(char_digit))
        return answer