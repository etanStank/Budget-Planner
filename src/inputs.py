"""
    Author: Rohan
    Date: 10/02/2025
    Description: Responsible for all of the inputs formatting.
"""

"""
specify all of the prefixes
    -o (One off items)
    -a (Constant income/expense over time (weekly))
    -t (Money added over time, requires a time rate, days, weeks, months, years)
    -c (Closes inout requests)
"""

"""multiprocessing module:
    inputs -> calculations
    calculations -> outputs
"""

# | ------------------------------------------------------------- | #

import multiprocessing

# | ------------------------------------------------------------- | #

def convert_string(input):
    list = [[],[]]
    input_list = input.split()

    for item in input_list:
        item_index = input_list.index(item)
        if item == "-":
            item_after = list[item_index + 1]
            if isinstance(item_after, str):
                list[0].append(str(item) + str(item_after))

    return list

# | ------------------------------------------------------------- | #

input_request = True

while input_request:
    input = input("Add your request: ")

    

    # send the correct data to calculations.


