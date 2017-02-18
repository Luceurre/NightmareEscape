class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def null(self):
        self.x = 0
        self.y = 0

    def __cmp__(self, other):
        return self.x == other.x and self.y == other.y

VECTOR_NULL = Vector(0, 0)

