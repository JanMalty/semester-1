"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Jan Malty
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input("Enter number of steps:"))  # read an integer number of steps (>0)
if maxtime < 0:
    print("put an integer higher than 0")

state = "red"
steps=0
num=0

while (maxtime+1) != systime:
    if steps == list(states.values())[num]:
        state = list(states.keys())[num+1]
        num += 1
        steps = 0
    print(f"Time {systime:03} State {state}")
    systime+=1
    steps+=1

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14