#!/usr/bin/python3
for num in range(1, 90):
    if num < 89:
        if num % 11 == 0:
            continue
        print('{:0>2}'.format(num), end=", ")
    else:
        print('{}'.format(num))
