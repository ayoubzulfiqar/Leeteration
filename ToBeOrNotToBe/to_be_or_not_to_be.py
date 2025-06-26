class Expectation:
    def __init__(self, val):
        self.val = val

    def toBe(self, other_val):
        if self.val == other_val:
            return True
        else:
            raise Exception("Not Equal")

    def notToBe(self, other_val):
        if self.val != other_val:
            return True
        else:
            raise Exception("Equal")

def expect(val):
    return Expectation(val)