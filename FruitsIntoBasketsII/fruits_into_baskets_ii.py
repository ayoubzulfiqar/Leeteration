def solve(fruits, baskets):
    n = len(fruits)
    
    is_basket_used = [False] * n
    
    unplaced_fruits_count = 0
    
    for i in range(n):
        current_fruit_quantity = fruits[i]
        
        placed_in_current_iteration = False
        
        for j in range(n):
            if not is_basket_used[j] and baskets[j] >= current_fruit_quantity:
                is_basket_used[j] = True
                placed_in_current_iteration = True
                break
        
        if not placed_in_current_iteration:
            unplaced_fruits_count += 1
            
    return unplaced_fruits_count