import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if x != y:
                new_weight = y - x
                heapq.heappush(max_heap, -new_weight)

        if not max_heap:
            return 0
        else:
            return -max_heap[0]