# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

from geometry import Circle,Point
c = Circle(5.0)
p_inside = Point(2.0, 2.0)
p_outside = Point(6.0, 6.0)

print(c)
print(p_inside in c)
print(p_outside in c)