class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        counts = {}
        for num in arr1:
            counts[num] = counts.get(num, 0) + 1

        result = []

        for num in arr2:
            if num in counts:
                while counts[num] > 0:
                    result.append(num)
                    counts[num] -= 1

        remaining_elements = []
        # Iterate through possible values to get them in ascending order
        # Constraints: 0 <= arr1[i], arr2[i] <= 1000
        for i in range(1001):
            if i in counts and counts[i] > 0:
                while counts[i] > 0:
                    remaining_elements.append(i)
                    counts[i] -= 1
        
        result.extend(remaining_elements)
        
        return result