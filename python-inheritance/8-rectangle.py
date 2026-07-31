#!/usr/bin/python3
"""
Contains Rectangle class that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class representation"""

    def __init__(self, width, height):
        """Instantiates Rectangle with validated width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
