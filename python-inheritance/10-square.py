#!/usr/bin/python3
"""
Contains Square class that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class representation"""

    def __init__(self, size):
        """Instantiates Square with validated size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
