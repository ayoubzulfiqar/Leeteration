class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nge_map = {}
        stack = []
        
        for i in range(len(nums2) - 1, -1, -1):
            current_num = nums2[i]
            
            while stack and stack[-1] <= current_num:
                stack.pop()
            
            if not stack:
                nge_map[current_num] = -1
            else:
                nge_map[current_num] = stack[-1]
            
            stack.append(current_num)
            
        ans = []
        for num in nums1:
            ans.append(nge_map[num])
            
        return ans