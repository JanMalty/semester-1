# Worksheet 1.2: Task 1 Solution
import sys

try:
    grade=int(input("enter an integer grade in the range 0 to 100:"))
    if grade < 0 or grade > 100:
        print("Error: Grade must be an integer between 0 and 100",file=sys.stderr)
        sys.exit()
    elif 0 <= grade < 40:
        print(grade,"is a Fail")
    elif 40 <= grade < 70:
        print(grade,"is a Pass")
    elif 70 <= grade <= 100:
        print(grade,"is a Distinction")
except ValueError:
    print("Error: Grade must be an integer between 0 and 100",file=sys.stderr)
    sys.exit()