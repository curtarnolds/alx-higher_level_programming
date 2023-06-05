#!/usr/bin/python3
"""A simple 3-say_my_name module.

say_my_name: Prints the name of the user in a sentence
"""


def say_my_name(first_name, last_name=''):
    """Print 'My name is `first_name` `last_name`.

    Arguments:
        first_name (str): The string to print as first name
        last_name (str): The string to print as last_name)

    Exceptions:
                Raises TypeError is either arguments are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')
