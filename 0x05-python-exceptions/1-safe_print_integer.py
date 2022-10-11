def safe_print_integer(value):
    """Print an integer with '{:d}'.format()"""
    try:
        print(f'{value:d}')
        return True
    except ValueError:
        return False
