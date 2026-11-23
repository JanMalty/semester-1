import random

# Get user to input how many random numbers they want
nums=int(input("Enter number of random number you want:"))
# Generate this many random numbers
list=[]
for i in range(nums):
    list.append(random.randint(0,100))
# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as file:
    for number in list:
        file.write(f"{number}\n")
