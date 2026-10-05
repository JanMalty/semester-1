# Worksheet 1.2: Task 2 Solution
import sys
import statistics

x=0
list=[]

while x==0 :
    try:
        val=0
        val=float(input("Enter a float value:"))
        list.append(val)
        x=int(input("Wanna exit? 1 or 0:"))
    except:
        print("Error: no numbers provided")
        sys.exit()

print(list)

print("Minimum =",min(list))
print("Maximum =",max(list))
print("Mean =",sum(list) / len(list))
print("Median =",statistics.median(list))