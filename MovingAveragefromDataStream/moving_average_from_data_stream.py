import collections

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = collections.deque()
        self.current_sum = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.current_sum += val

        if len(self.window) > self.size:
            oldest_val = self.window.popleft()
            self.current_sum -= oldest_val
        
        return self.current_sum / len(self.window)