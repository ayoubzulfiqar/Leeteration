import collections

class RecentCounter:

    def __init__(self):
        self.requests = collections.deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)