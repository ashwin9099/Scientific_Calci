import math
class CalculatorModel:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)

    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def tan(self, a):
        return math.tan(math.radians(a))

    def log(self, a):
        if a <= 0:
            raise ValueError("Logarithm is only defined for positive numbers")
        return math.log10(a)

    def ln(self, a):
        if a <= 0:
            raise ValueError("Natural log is only defined for positive numbers")
        return math.log(a)