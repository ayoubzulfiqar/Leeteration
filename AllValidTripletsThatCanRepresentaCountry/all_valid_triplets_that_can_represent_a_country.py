import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_valid_triplets_for_country(nums):
    n = len(nums)
    if n < 3:
        return []

    nums.sort()
    
    valid_triplets = []
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        for j in range(i + 1, n - 1):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
                
            for k in range(j + 1, n):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                    
                current_sum = nums[i] + nums[j] + nums[k]
                
                if is_prime(current_sum):
                    valid_triplets.append([nums[i], nums[j], nums[k]])
                    
    return valid_triplets