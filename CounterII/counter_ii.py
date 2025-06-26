class Counter:
    def __init__(self, init_value: int):
        self._initial_value = init_value
        self._current_value = init_value

    def increment(self) -> int:
        self._current_value += 1
        return self._current_value

    def decrement(self) -> int:
        self._current_value -= 1
        return self._current_value

    def reset(self) -> int:
        self._current_value = self._initial_value
        return self._current_value

def createCounter(init: int) -> Counter:
    return Counter(init)