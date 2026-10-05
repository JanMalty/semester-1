# Worksheet 1.2: Task 1 Solution
import sys

integer=int(input("enter an integer grade in the range 0 to 100:"))

if 0 <= integer < 40:
    print(integer,"is a Fail")
elif 40 <= integer < 70:
    print(integer,"is a Pass")
elif 70 <= integer <= 100:
    print(integer,"is a Distinction")
else:
    print("Error: Grade must be an integer between 0 and 100")
    sys.exit("Error!")