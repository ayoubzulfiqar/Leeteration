class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer_elements(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._transfer_elements()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer_elements()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack