class MyHashSet:

    def __init__(self):
        self.storage = [False] * 1000001

    def add(self, key: int) -> None:
        self.storage[key] = True

    def remove(self, key: int) -> None:
        self.storage[key] = False

    def contains(self, key: int) -> bool:
        return self.storage[key]