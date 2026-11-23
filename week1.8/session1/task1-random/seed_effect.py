# See README.md for instructions on what to do this program

import random

random.seed(1)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

# Sets the seed for the random number generator so that the same sequence of random numbers is produced each time the program runs.
# Makes it easier to debug code becuase there is expected results
