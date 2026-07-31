#!/usr/bin/python3
"""
Module defining the MyList class.
"""


class MyList(list):
    """A subclass of list that adds sorted printing functionality."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
