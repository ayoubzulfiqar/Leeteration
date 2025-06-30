class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def has_distinct_elements(arr: list[int]) -> bool:
            """
            Checks if all elements in the given array are distinct.
            An empty array is considered to have distinct elements.
            """
            return len(arr) == len(set(arr))

        n = len(nums)

        # Iterate through the possible number of operations, starting from 0.
        # Each operation removes 3 elements from the beginning.
        # We need to find the minimum 'k' such that after 'k' operations,
        # the remaining array has distinct elements.
        # The maximum number of operations needed would be to remove all elements,
        # which is ceil(n / 3). The loop range covers this and more to be safe.
        # For example, if n = 100, n // 3 + 2 = 33 + 2 = 35.
        # k will go from 0 to 34, covering all necessary scenarios where
        # start_idx can go up to 34 * 3 = 102, ensuring remaining_array becomes empty.
        for k in range(0, n // 3 + 2):
            start_idx = k * 3
            
            remaining_array = []
            # If start_idx is less than n, there are elements remaining.
            if start_idx < n:
                remaining_array = nums[start_idx:]
            
            # Check if the remaining part of the array has distinct elements.
            if has_distinct_elements(remaining_array):
                return k
        
        # This line should theoretically not be reached because an empty array
        # (which will eventually be formed after enough operations) is always
        # considered to have distinct elements, and the loop covers this case.
        return -1