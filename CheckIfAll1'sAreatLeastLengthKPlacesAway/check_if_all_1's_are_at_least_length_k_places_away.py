class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last_one_idx = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if last_one_idx != -1:
                    if (i - last_one_idx - 1) < k:
                        return False
                last_one_idx = i
        return True