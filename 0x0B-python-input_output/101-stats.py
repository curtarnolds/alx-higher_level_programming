#!/usr/bin/python3
"""Python script to read stdin line by line and compute metrics."""
import sys

input_line = []
count_line = 0
total_size = 0
for line in sys.stdin:
    count_line += 1
    line = line.strip()
    words = line.split()
    

    if count_line % 10 == 0:
        print(f"File size: {total_size}")
