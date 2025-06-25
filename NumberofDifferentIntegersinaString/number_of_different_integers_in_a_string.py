```python
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        num_str = ""
        for char in word:
            if char.isdigit():
                num_str += char
            else:
                if num_str:
                    nums.add(int(num_str))
                    num_str = ""
        if num_str:
            nums.add(int(num_str))
        return len(nums)
```