class TwoSum:

    def __init__(self):
        self.counts = {}

    def add(self, number: int) -> None:
        self.counts[number] = self.counts.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for num1 in self.counts:
            num2 = value - num1
            if num1 == num2:
                if self.counts[num1] >= 2:
                    return True
            else:
                if num2 in self.counts:
                    return True
        return False