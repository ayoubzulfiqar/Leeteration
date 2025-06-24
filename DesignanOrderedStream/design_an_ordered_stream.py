class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * (n + 1)
        self.ptr = 1
        self.n = n

    def insert(self, idKey: int, value: str) -> list[str]:
        self.data[idKey] = value
        
        chunk = []
        while self.ptr <= self.n and self.data[self.ptr] is not None:
            chunk.append(self.data[self.ptr])
            self.ptr += 1
            
        return chunk