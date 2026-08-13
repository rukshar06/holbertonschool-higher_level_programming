#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    for args in sys.argv[1:]:
        total += int(args)
    print(total)
