def findSneakyNumbers(nums: list[int]) -> list[int]:
    n = len(nums) - 2
    
    counts = [0] * n
    
    for num in nums:
        counts[num] += 1
        
    sneaky_numbers = []
    
    for i in range(n):
        if counts[i] == 2:
            sneaky_numbers.append(i)
            if len(sneaky_numbers) == 2:
                break
                
    return sneaky_numbers