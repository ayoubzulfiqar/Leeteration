def find_k_or(nums: list[int], k: int) -> int:
    result = 0
    for i in range(32):  # Iterate through bit positions from 0 to 31
        count = 0
        for num in nums:
            if (num >> i) & 1:  # Check if the i-th bit is set in num
                count += 1
        if count >= k:  # If at least k numbers have the i-th bit set
            result |= (1 << i)  # Set the i-th bit in the result
    return result