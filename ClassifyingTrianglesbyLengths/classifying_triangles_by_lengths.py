class TriangleClassifier:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def classify(self):
        sides = sorted([self.side1, self.side2, self.side3])
        a, b, c = sides[0], sides[1], sides[2]

        if a <= 0:
            return "invalid"

        if a + b <= c:
            return "invalid"

        if a == b and b == c:
            return "equilateral"
        elif a == b or b == c:
            return "isosceles"
        else:
            return "scalene"