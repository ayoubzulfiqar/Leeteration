class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        s = min(start, destination)
        d = max(start, destination)

        dist1 = sum(distance[s:d])

        total_dist = sum(distance)

        dist2 = total_dist - dist1

        return min(dist1, dist2)