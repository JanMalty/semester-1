# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
#keeps looping as long as the list contains items.
#.pop() removes and prints the last item each time until the list is empty.

# What features of Python does it rely on?
#It relies on while loops, lists, the .pop() method and Python's Boolean values.