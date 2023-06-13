#!/usr/bin/python3
"""A script that adds all arguments to a Python list,
and saves them to a file
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file').load_from_json_file

filename = "add_item.json"
list_obj = []

try:
    list_obj = load_from_json_file(filename)
except FileNotFoundError:
    pass

for item in sys.argv[1:]:
    list_obj.append(item)
save_to_json_file(list_obj, filename)
