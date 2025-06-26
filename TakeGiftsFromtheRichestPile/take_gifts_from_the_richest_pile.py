import heapq

def gifts_remaining(gifts: list[int], k: int) -> int:
    """
    Calculates the total number of gifts remaining after k seconds.

    Args:
        gifts: A list of integers representing the number of gifts in various piles.
        k: An integer representing the number of seconds.

    Returns:
        The total number of gifts remaining after k seconds.
    """
    # Use a min-heap to simulate a max-heap by storing negative values.
    # This allows efficient retrieval of the pile with the maximum number of gifts.
    max_heap = []
    for g in gifts:
        heapq.heappush(max_heap, -g)

    for _ in range(k):
        # Get the pile with the maximum number of gifts (most negative value)
        current_max_gifts = -heapq.heappop(max_heap)

        # Reduce the number of gifts to the floor of its square root
        new_gifts = int(current_max_gifts**0.5)

        # Push the new number of gifts back into the heap (as a negative value)
        heapq.heappush(max_heap, -new_gifts)

    # Sum the remaining gifts (remembering they are stored as negative values)
    total_remaining_gifts = 0
    while max_heap:
        total_remaining_gifts += -heapq.heappop(max_heap)

    return total_remaining_gifts