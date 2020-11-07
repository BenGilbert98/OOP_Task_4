from calculator_class import Calculator

answer = Calculator() # object created of class Calculator

# input from user to determine which method to use
method = input(f"Which method would you like to use? {answer.methods}        ")
# the first 5 methods use 2 numbers so if in that range it prompts the user for these numbers
if method in answer.methods[0:5]:
    num1 = int(input("Please enter 1st number "))
    num2 = int(input("Please enter 2nd number "))
    if method == "Add":
        answer.add(num1, num2)
    if method == "Subtract":
        answer.subtract(num1, num2)
    if method == "Multiply:":
        answer.multiply(num1, num2)
    if method == "Divide":
        answer.divide(num1, num2)
    if method == "Divisible":
        answer.divisible(num1, num2)
    # this method requires the length of the base and height and so the user is prompted for these values
if method in "Area of Triangle":
    a = float(input("Please enter the length of the base    "))
    b = float(input("Please enter the height of the triangle    "))
    answer.area_of_triangle(a, b)
if method in "Inch/Cm Conversion":
    # prompts the user if they want to convert from cm to inch or the other way around
    conversion_type = input("Which conversion would you like to use? a) cm --> inch    b) inch --> cm       ")
    if conversion_type == "a":
        cm = float(input("Enter value to be converted   "))
        answer.conversion_cm_inch(cm)
    if conversion_type == "b":
        inch = float(input("Enter value to be converted   "))
        answer.conversion_inch_cm(inch)
