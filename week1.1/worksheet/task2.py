"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Jan Malty
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer. DONE
try:
    amount=int(input("How much you want to save every month?"))
# Validate that they have entered an integer.
except:
    print("Invalid amount")
    exit()
    

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12). DONE
TotalPerYear=amount*12
# print this out for the user with a suitable message. DONE
print(TotalPerYear,"is the amount you will have saved by the end of the year.")


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year. DONE
FinalTotal=TotalPerYear*1.008
# print this out in the format £X.XX (to two decimal places). DONE
print(f"Total Saved Per Year (Including interest):£{FinalTotal:.2f}")

