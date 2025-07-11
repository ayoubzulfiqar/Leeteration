import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]