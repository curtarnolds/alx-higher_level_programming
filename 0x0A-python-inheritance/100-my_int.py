#!/usr/bin/python3
"""A MyInt module."""


class MyInt(int):
    """A class that inherits from int."""

    def __eq__(self, value: object) -> bool:
        """Redefines equality of MyInt."""
        return False

    def __ne__(self, value):
        """Redefines inequality of MyInt."""
        return True
