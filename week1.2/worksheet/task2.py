# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    print("Error: no numbers provided", file=sys.stderr)
    sys.exit()

numbers.sort()

if len(numbers) % 2 == 1:
    median = numbers[len(numbers) // 2]
else:
    middle1 = numbers[(len(numbers) // 2) -1]
    middle2 = numbers[len(numbers) // 2]
    median = (middle1 + middle2) / 2

print("Minimum =", min(numbers))
print("Maximum =", max(numbers))
print("Mean =", sum(numbers) / len(numbers))
print("Median =", median)