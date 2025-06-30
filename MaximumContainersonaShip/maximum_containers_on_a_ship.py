def maxContainers(n: int, w: int, maxWeight: int) -> int:
    """
    Calculates the maximum number of containers that can be loaded onto a ship.

    Args:
        n: The dimension of the n x n cargo deck.
        w: The weight of a single container.
        maxWeight: The maximum total weight capacity of the ship.

    Returns:
        The maximum number of containers that can be loaded.
    """
    total_cells = n * n
    max_containers_by_weight = maxWeight // w
    return min(total_cells, max_containers_by_weight)

if __name__ == '__main__':
    # Example 1
    n1 = 2
    w1 = 3
    maxWeight1 = 15
    result1 = maxContainers(n1, w1, maxWeight1)
    print(result1) # Expected Output: 4

    # Example 2
    n2 = 3
    w2 = 5
    maxWeight2 = 20
    result2 = maxContainers(n2, w2, maxWeight2)
    print(result2) # Expected Output: 4

    # Additional test case: weight capacity is very high, limited by cells
    n3 = 5
    w3 = 10
    maxWeight3 = 1000
    result3 = maxContainers(n3, w3, maxWeight3)
    print(result3) # Expected Output: 25 (5*5=25 cells, 1000/10=100 containers by weight, min(25, 100) = 25)

    # Additional test case: cells are many, limited by weight
    n4 = 10
    w4 = 100
    maxWeight4 = 500
    result4 = maxContainers(n4, w4, maxWeight4)
    print(result4) # Expected Output: 5 (10*10=100 cells, 500/100=5 containers by weight, min(100, 5) = 5)

    # Edge case: maxWeight is less than w
    n5 = 2
    w5 = 10
    maxWeight5 = 5
    result5 = maxContainers(n5, w5, maxWeight5)
    print(result5) # Expected Output: 0 (5//10 = 0)

    # Edge case: n=1, w=1, maxWeight=1
    n6 = 1
    w6 = 1
    maxWeight6 = 1
    result6 = maxContainers(n6, w6, maxWeight6)
    print(result6) # Expected Output: 1 (1*1=1 cell, 1//1=1 container by weight, min(1,1)=1)