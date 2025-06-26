class ArrayWrapper:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def __add__(self, other: 'ArrayWrapper') -> int:
        return sum(self.nums) + sum(other.nums)

    def __str__(self) -> str:
        return "[" + ",".join(map(str, self.nums)) + "]"