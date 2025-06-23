import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self) -> None:
        print("first")
        self.first_done.set()

    def second(self) -> None:
        self.first_done.wait()
        print("second")
        self.second_done.set()

    def third(self) -> None:
        self.second_done.wait()
        print("third")