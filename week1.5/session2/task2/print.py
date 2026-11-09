# Week 1.5, Session 2: Task 2

# Write code here to create and print a Point object,
# then create and print a Circle object
from geometry import Point, Circle

p1 = Point(3.0, 4.0)
print(p1)  

custom_centre = Point(1.0, 2.0)

c1 = Circle(5.0, custom_centre)
print(c1) 

print(f"Area of circle: {c1.area():.2f}")