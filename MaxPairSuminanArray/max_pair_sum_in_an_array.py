import collections

class Solution:
    def get_largest_digit(self, num: int) -> int:
        max_digit = 0
        s_num = str(num)
        for char_digit in s_num:
            digit = int(char_digit)
            if digit > max_digit:
                max_digit = digit
        return max_digit

    def maxSum(self, nums: list[int]) -> int:
        digit_to_nums_map = collections.defaultdict(list)

        for num in nums:
            largest_digit = self.get_largest_digit(num)
            digit_to_nums_map[largest_digit].append(num)

        max_pair_sum = -1

        for num_list in digit_to_nums_map.values():
            if len(num_list) >= 2:
                num_list.sort(reverse=True)
                current_pair_sum = num_list[0] + num_list[1]
                if current_pair_sum > max_pair_sum:
                    max_pair_sum = current_pair_sum
        
        return max_pair_sum