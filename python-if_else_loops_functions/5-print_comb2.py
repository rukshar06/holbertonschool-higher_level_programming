#!/usr/bin/python3
for number in range(0, 100):
    print("{:2d}".format(number), end="\n" if number == 99 else ", ")
