class Calculator:
    def __init__(self, initial_value: float):
        self._result = float(initial_value)

    def add(self, value: float):
        self._result += value
        return self

    def subtract(self, value: float):
        self._result -= value
        return self

    def multiply(self, value: float):
        self._result *= value
        return self

    def divide(self, value: float):
        if value == 0:
            raise Exception("Division by zero is not allowed")
        self._result /= value
        return self

    def power(self, value: float):
        self._result **= value
        return self

    def getResult(self) -> float:
        return self._result