#!/usr/bin/env python3

import math

print("Welcome to Pythagorean Theorem Calculator!")
print("Calculate the sides of your triangle.")
print("\n You have three sides of a triangle (a,b,c), where c is your hypotenuse (opposite side of the right triangle)")

def main:

side = input("Which side (a,b,c,) are you trying to solve for? side: ")

if side == "a" :
    b_side = int(input("Enter the value of b: ")
    c_side = int(input("Enter the value of c: ")
    a_side = math.sqrt(c_side ** 2 - b_side ** 2)
    print("The value of side a is: " + aside)

elif side == "b"
    a_side = int(input("Enter the value of a: ")
    c_side = int(input("Enter the value of c: ")
    b_side = math.sqrt(c_side ** 2 - a_side ** 2)
    print("The value of side b is: " + b_side)

elif side == "c"
    a_side = int(input("Enter the value of a: ")
    b_side = int(input("Enter the value of b: ")
    c_side = math.sqrt(a_side ** 2 + b_side ** 2)
    print("The value of side c is: " + c_side)

else:
    print("Invalid input, please select a, b or c.")

if __name__ == "__main__":
main()
