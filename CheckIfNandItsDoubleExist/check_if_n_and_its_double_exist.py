class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()
        for x in arr:
            # Check if x is double of a number already seen (i.e., x = 2 * y, where y is in seen)
            # This means we are looking for y = x / 2
            if x % 2 == 0 and (x // 2) in seen:
                return True
            
            # Check if x is half of a number already seen (i.e., y = 2 * x, where y is in seen)
            # This means we are looking for y = 2 * x
            if (2 * x) in seen:
                return True
            
            seen.add(x)
        
        return False