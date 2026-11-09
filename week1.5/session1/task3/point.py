# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self):
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, other):
        """
        Returns distance of this Point from another Point.
        """
        return math.hypot(self.x - other.x, self.y - other.y)



# Finally, add code here to demonstrate use of Point
p1 = Point(3.0, 4.0)
p2 = Point(6.0, 8.0)

print(p1.x, p1.y)
print(p1.distance())
print(p1.distance_to(p2))