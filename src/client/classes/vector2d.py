

class Vector2d:
    def __init__(self, x, y):
       self.x, self.y = x, y

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"

    def getTupple(self):
        return (self.x,self.y)
        