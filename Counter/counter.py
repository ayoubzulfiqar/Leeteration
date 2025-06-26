def createCounter(n: int):
    current_value = n
    def counter():
        nonlocal current_value
        val = current_value
        current_value += 1
        return val
    return counter