# Homework 1 – Beginner Version (clean and simple)
import math

# 1. Given a side of a square. Find its perimeter and area.
while True:
    try:
        a = float(input("Enter the side of the square: "))
        P = 4 * a
        S = a ** 2
        print("Perimeter is:", P)
        print("Area is:", S)
        break
    except ValueError:
        print("Please enter a number!")
print()  # blank line for readability


# 2. Given diameter of a circle. Find its length (circumference).
while True:
    try:
        d = float(input("Enter the diameter of the circle: "))
        L = math.pi * d
        print("Length (circumference) is:", L)
        break
    except ValueError:
        print("Please enter a number!")
print()


# 3. Given two numbers a and b. Find their mean.
while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        mean = (a + b) / 2
        print("Mean is:", mean)
        break
    except ValueError:
        print("Please enter valid numbers!")
print()


# 4. Given two numbers a and b. Find their sum, product, and squares of each number.
while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        sum_ab = a + b
        product_ab = a * b
        square_a = a ** 2
        square_b = b ** 2
        print("Sum is:", sum_ab)
        print("Product is:", product_ab)
        print("Square of first number is:", square_a)
        print("Square of second number is:", square_b)
        break
    except ValueError:
        print("Please enter valid numbers!")
print("Homework complete!")
