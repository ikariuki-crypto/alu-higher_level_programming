#!/usr/bin/python3
"""Module that defines a sqaure classs with validated siZe."""


class Square:
    """Defines a sqaure with validated size attribute."""

    def --init--(self, size=0):
        """Intialize a new Square.

        Args:
        size (int): The size of the sqaure (default 0).

        Raises:
           TypeError: If size is not an integer
           ValueError: If size is less than 0

        """
        if not insinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=o")
        self.--size = size
