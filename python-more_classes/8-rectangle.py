#!/usr/bin/python3
"""Defines a module for Rectangle with static method for comparison."""


class Rectangle:
    """Class that defines a rectangle and compares instances by area."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value (int): The width value.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Args:
            value (int): The height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for _ in range(self.__height):
            rect.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """Return string representation to recreate instance with eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message when deleted and decrement instance counter."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area.

        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle instance.

        Returns:
            Rectangle: rect_1 if areas are equal, else the larger instance.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
