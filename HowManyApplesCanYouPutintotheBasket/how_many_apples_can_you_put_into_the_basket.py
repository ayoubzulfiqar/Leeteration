def maxNumberOfApples(weight: list[int]) -> int:
    weight.sort()
    
    current_weight = 0
    count = 0
    basket_capacity = 5000
    
    for w in weight:
        if current_weight + w <= basket_capacity:
            current_weight += w
            count += 1
        else:
            break
            
    return count