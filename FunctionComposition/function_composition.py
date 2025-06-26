def compose(functions):
    def composed_function(x):
        if not functions:
            return x
        
        current_value = x
        for func in reversed(functions):
            current_value = func(current_value)
            
        return current_value
        
    return composed_function