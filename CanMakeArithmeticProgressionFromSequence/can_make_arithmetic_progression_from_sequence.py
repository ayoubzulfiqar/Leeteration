class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        
        if len(arr) < 2:
            return True 
        
        common_difference = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != common_difference:
                return False
                
        return True