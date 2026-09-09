#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    # create a dictionary
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
# create result
    total = 0
    previous = 0
# loop through elements of roman_string
    for letter in reversed(roman_string.upper()):
        # change element to its value
        current = values.get(letter, 0)
# check if current element isnt smaller than the next
        if current < previous:
            # if yes; subtract
            total -= current
        else:
    # add
            total += current

        previous = current
# add
    return total
