class MyHashMap:

    def __init__(self):
        self.capacity = 2069
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                pair[1] = value
                return
        
        bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        
        return -1

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                return