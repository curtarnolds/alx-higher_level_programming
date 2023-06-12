#!/usr/bin/python3
"""A simple 1-my_list module."""


class MyList(list):
    """A simple class that inherits from `list`."""
    def print_sorted(self):
        """Prints the list, but sorted."""
        dup_list = self[:]
        dup_list.sort()
        print(dup_list)
