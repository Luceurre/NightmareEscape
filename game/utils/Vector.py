import math


class Vector:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def null(self):
        self.x = 0
        self.y = 0

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise KeyError

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def get_theta(self):
        return math.atan2(self.y, self.x)

VECTOR_NULL = Vector(0, 0)

