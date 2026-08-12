#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    count = len(args)

    if count == 1:
        label = "argument"
    else:
        label = "arguments"

    if count == 0:
        punctuation = "."
    else:
        punctuation = ":"

    print("{} {}{}".format(count, label, punctuation))

    for i in range(count):
        print("{}: {}".format(i + 1, args[i]))
