#!/usr/bin/python3
for n in range(9):
    for x in range(n + 1, 10):
        if n * 10 + x < 89:
            print("{:d}{:d}".format(n, x), end=", ")
print("{:d}".format(89))
