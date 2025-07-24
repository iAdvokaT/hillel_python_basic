from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.a = a
        self.b = b

    def get_simplified(self):
        """Повертає спрощену копію дробу"""
        common = gcd(self.a, self.b)
        return Fraction(self.a // common, self.b // common)

    def __add__(self, other):
        num = self.a * other.b + other.a * self.b
        denom = self.b * other.b
        return Fraction(num, denom)

    def __sub__(self, other):
        num = self.a * other.b - other.a * self.b
        denom = self.b * other.b
        return Fraction(num, denom)

    def __mul__(self, other):
        num = self.a * other.a
        denom = self.b * other.b
        return Fraction(num, denom)

    def __eq__(self, other):
        f1 = self.get_simplified()
        f2 = other.get_simplified()
        return f1.a == f2.a and f1.b == f2.b

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)       # 2/3
f_b = Fraction(3, 6)       # 3/6

f_c = f_b + f_a            # (3*3 + 2*6) / 6*3 = (9+12)/18 = 21/18
assert str(f_c) == 'Fraction: 21, 18'

f_d = f_b * f_a            # (3*2)/(6*3) = 6/18
assert str(f_d) == 'Fraction: 6, 18'

f_e = f_a - f_b            # (2*6 - 3*3)/18 = (12-9)/18 = 3/18
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c           # True
assert f_d > f_e           # True
assert f_a != f_b          # True

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2          # True

print('OK')