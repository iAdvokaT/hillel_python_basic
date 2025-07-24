import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_square = self.get_square() + other.get_square()
            side = int(math.sqrt(new_square))
            # Підбираємо сторони, щоб площа дорівнювала потрібній
            while new_square % side != 0:
                side -= 1
            return Rectangle(side, new_square // side)
        raise TypeError("Можна додавати лише об'єкти Rectangle")

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            new_square = self.get_square() * n
            side = int(math.sqrt(new_square))
            while new_square % side != 0:
                side -= 1
            return Rectangle(side, int(new_square // side))
        raise TypeError("Множити можна лише на число")

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"

r1 = Rectangle(2, 4)      # площа 8
r2 = Rectangle(3, 6)      # площа 18
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2              # площа 26
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4               # площа 32
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'  # 18 == 18

print("Усі тести пройдені успішно!")