#!/usr/bin/python3


def no_c(my_string):
    copy_str = [x for x in my_string if x not in 'cC']
    return ("".join(copy_str))
