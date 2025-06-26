class Solution:
    def reduce(self, nums: list[int], fn: callable, init: int) -> int:
        if not nums:
            return init

        val = init
        for num in nums:
            val = fn(val, num)
        return val