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

import budget_planner

# | ------------------------------------------------------------- | #

def convert_string(user_input):
    # Converts the initial input into a multidimensional list which seperates the prefix from the request.
    # Doesn't check edge cases but eh, should check for all prefixes...
    list = [[],[]]
    input_list = user_input.split()
    
    for item in input_list:
        item_index = input_list.index(item)
        if item == "-":
            item_after = list[item_index + 1]
            if isinstance(item_after, str):
                if item_after in budget_planner.__prefixes__:
                        list[0].append(str(item) + str(item_after))
    return list

# | ------------------------------------------------------------- | #

def input_request():
    user_input = input("Add your request: ")
    convert_string(user_input)
    # send info over to calculations
    # tell the main py file to not request input until it is complete with calculations

# | ------------------------------------------------------------- | #

