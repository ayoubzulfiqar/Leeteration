class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        def count_set_bits(n: int) -> int:
            count = 0
            while n > 0:
                n &= (n - 1)
                count += 1
            return count

        result = []
        for h in range(12):
            for m in range(60):
                if count_set_bits(h) + count_set_bits(m) == turnedOn:
                    minute_str = str(m).zfill(2)
                    result.append(f"{h}:{minute_str}")
        return result