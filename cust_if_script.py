#!/usr/bin/env python3

score=int(input("Enter your score: "))

letter_grade = ""

if score >=90:
    print("Congratulations!!! You have an A!")
elif score >=80:
    print("Great job!! You have a B!")
elif score >=70:
    print("Keep up the hardwork! Stay motivated! You have a C!")
elif score >=60:
    print("Need improvement! Submit any missing assignments and/or reach out for assistance. You have a D")
elif score <60:
    print("You are currently failing the course! You have an F. Come see me.")

print(letter_grade)
