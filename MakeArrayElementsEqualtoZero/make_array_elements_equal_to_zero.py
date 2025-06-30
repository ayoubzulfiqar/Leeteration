import copy

class Solution:
    def makeArrayElementsEqualtoZero(self, nums: list[int]) -> int:
        n = len(nums)
        valid_selections_count = 0

        for i in range(n):
            if nums[i] == 0:
                for initial_dir in [1, -1]:
                    current_nums = copy.deepcopy(nums)
                    curr = i
                    direction = initial_dir

                    while 0 <= curr < n:
                        if current_nums[curr] == 0:
                            curr += direction
                        else:
                            current_nums[curr] -= 1
                            direction *= -1
                            curr += direction
                    
                    all_zeros = True
                    for val in current_nums:
                        if val != 0:
                            all_zeros = False
                            break
                    
                    if all_zeros:
                        valid_selections_count += 1
        
        return valid_selections_count