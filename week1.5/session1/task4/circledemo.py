# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

"""
Classes for working with two-dimensional geometry.
"""

import math

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y

    def distance(self):
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, other):
        """
        Returns distance of this Point from another Point.
        """
        return math.hypot(self.x - other.x, self.y - other.y)


class Circle:
    """
    A circle, with a radius and centre coordinates.
    """

    def __init__(self, radius, centre=Point(0.0, 0.0)):
        """
        Creates a Circle, given values for radius & centre coordinates.
        """
        self.radius = radius
        self.centre = centre

    def area(self):
        """
        Returns the area of this Circle.
        """
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """
        Returns the perimeter of this Circle.
        """
        return 2.0 * math.pi * self.radius