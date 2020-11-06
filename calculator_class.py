class Calculator:

    def __init__(self):
        self.methods = ["Add", "Subtract", "Multiply", "Divide", "Divisible", "Area of Triangle", "Inch/Cm Conversion"]

    def add(self, num1, num2):
        return print(f"{num1} + {num2} = ", num1 + num2)

    def subtract(self, num1, num2):
        return print(f"{num1} - {num2} = ", num1 - num2)

    def multiply(self, num1, num2):
        return print(f"{num1} * {num2} = ", num1*num2)

    def divide(self, num1, num2):
        return print(f"{num1} / {num2} = ", num1/num2)

    def divisible(self, num1, num2):
        if num1 % num2 == 0:
            return print(f"{num1} is divisible by {num2}")
        elif num1 % num2 != 0:
            return print(f"{num1} is not divisible by {num2}")

    def area_of_triangle(self, a, b):
        return print(0.5 * a * b)

    def conversion_cm_inch(self, cm):
        return print(f"{cm}cm is equal to", cm/2.54, "inches")

    def conversion_inch_cm(self, inch):
        return print(f"{inch}inch is equal to", inch * 2.54, "cm")