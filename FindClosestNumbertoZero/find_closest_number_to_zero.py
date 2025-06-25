```python
def find_closest_number_to_zero(nums):
    closest_num = nums[0]
    min_distance = abs(nums[0])
    
    for num in nums:
        distance = abs(num)
        
        if distance < min_distance:
            min_distance = distance
            closest_num = num
        elif distance == min_distance:
            closest_num = max(closest_num, num)
            
    return closest_num
```