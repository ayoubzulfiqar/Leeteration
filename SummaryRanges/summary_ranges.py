class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        result = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            j = i

            # Find the end of the current continuous range
            while j + 1 < n and nums[j+1] == nums[j] + 1:
                j += 1

            end = nums[j]

            # Format the range string
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")

            # Move to the next element after the current range
            i = j + 1
            
        return result