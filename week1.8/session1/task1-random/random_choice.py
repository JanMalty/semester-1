import random

# Read names from a file
with open("names.txt") as infile:
    names = [line.strip() for line in infile]

# Ask user to enter how many names they want
number = int(input("How many names would you like?"))

# Randomly select that many names without duplicates
chosen_names = random.sample(names, number)

# Display the chosen names, one per line
for name in chosen_names:
    print(name)
