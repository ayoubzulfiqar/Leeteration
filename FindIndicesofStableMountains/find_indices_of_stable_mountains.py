class Solution:
    def findStableMountains(self, height: list[int], threshold: int) -> list[int]:
        stable_mountains_indices = []
        n = len(height)
        for i in range(1, n):
            if height[i - 1] > threshold:
                stable_mountains_indices.append(i)
        return stable_mountains_indices