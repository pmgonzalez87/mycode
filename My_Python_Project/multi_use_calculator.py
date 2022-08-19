#!/usr/bin/env python3

# Program make a simple calculator

from pyfiglet import Figlet
from termcolor import colored
import math

# This function adds two numbers
def add():
    print("************************************")
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    total = ( num1 + num2 )
    print("\n", num1, "+", num2, "=", total)
    input("\nPress Enter to continue...")

# This function subtracts two numbers
def subtract():
    print("************************************")
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    total = ( num1 - num2 )
    print(num1, "-", num2, "=", total)    
    input("\nPress Enter to continue...")

# This function multiplies two numbers
def multiply():
    print("************************************")
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    total = ( num1 * num2 )
    print(num1, "*", num2, "=", total)
    input("\nPress Enter to continue...")

# This function divides two numbers
def divide():
    print("************************************")
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    total = ( num1 / num2 )
    print(num1, "/", num2, "=", total)
    input("\nPress Enter to continue...")

# This function solves for Pythagorean Theorem
def pythagorean():
    side = input("\n Which side (a,b,c,) are you trying to solve for? side: ")
    side = side.lower()

    if side == "a":
        b_side = float(input("Enter the value of side b: "))
        c_side = float(input("Enter the value of hypotenuse c: "))
        a_side = math.sqrt(c_side ** 2 - b_side ** 2)
        print("The value of side a is: " + str(a_side))
        input("\nPress Enter to continue...")

    elif side == "b":
        a_side = float(input("Enter the value of side a: "))
        c_side = float(input("Enter the value of hypotenuse c: "))
        b_side = math.sqrt(c_side ** 2 - a_side ** 2)
        print("The value of side b is: " + str(b_side))
        input("\nPress Enter to continue...")

    elif side == "c":
        a_side = float(input("Enter the value of side a: "))
        b_side = float(input("Enter the value of side b: "))
        c_side = math.sqrt(a_side ** 2 + b_side ** 2)
        print("The value of hypotenuse c is: " + str(c_side))
        input("\nPress Enter to continue...")

# Title Banner
def title():
    f = Figlet(font='doom')
    print(colored(f.renderText('Welcome   to Calculator 2 . 0'), 'red'))
    f1 = Figlet(font='mnemonic')
    print(colored(f1.renderText('Created_by:_Paul_Gonzalez'), 'cyan'))

# Selection menu for the user
def selection_menu():
    f2 = Figlet(font='digital')
    print(colored(f2.renderText("Please select your math operation"), 'white'))
    print("1.Additiom")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Pythagorean Theorem")

# Instructions for using formula
def pyth_instr():
    print("************************************")
    print("\nCalculate the sides of your triangle.")
    print("\nYou have three sides of a triangle (a,b,c), where c is your \nhypotenuse (the side opposite of the right angle)")

# Main Calculator Loop
def calculator():
    title()

    while True:
        try:
            # presents the user with selection menu
            selection_menu()
            
            # takes the input from the user
            choice = input("\nEnter choice(1/2/3/4/5): ")
        
            # checks if choice is one of the four options
            if choice in ('1', '2', '3', '4', '5'):
        
                if choice == '1':
                    add()
        
                elif choice == '2':
                    subtract()
        
                elif choice == '3':
                    multiply()
        
                elif choice == '4':
                    divide()
                    
                elif choice == '5':
                    pyth_instr()
                    pythagorean()
                    
                # checks if user wants another calculation
                # breaks the while loop if user's input is no
                next_calculation = input("\nWould you like to solve another calculation? (yes/no): ")
                if next_calculation == "no":
                    print("Thank you for using the calculator!")
                    break
                
            else:
                print("Invalid Input")
            
        except ZeroDivisionError as err:
            print("Handling run-time error:", err)
        except ValueError as err:
            print("That was not a legal value for division:", err)
        # general error handling
        # a practical use might be exceptions we haven't designed solution for yet
        except Exception as err:
            # sys.exc_info returns a 3 tuple with into about the exception handled
            print("We did not anticipate that:", err)
            # raise by itself simply calls the previous exception that was thrown
            raise
calculator()
