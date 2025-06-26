class Solution:
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        seen = []
        ans = []
        k_consecutive_neg_ones = 0

        for num in nums:
            if num != -1:
                seen.insert(0, num)
                k_consecutive_neg_ones = 0
            else:
                k_consecutive_neg_ones += 1
                if k_consecutive_neg_ones <= len(seen):
                    ans.append(seen[k_consecutive_neg_ones - 1])
                else:
                    ans.append(-1)
        
        return ans