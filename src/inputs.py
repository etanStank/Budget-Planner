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

__prefixes__ = ["o", "a", "t", "c"]
__list__ = None

# | ------------------------------------------------------------- | #

def convert_string(user_input):
    # Converts the initial input into a multidimensional list which seperates the prefix from the request.
    # Doesn't check edge cases but eh, should check for all prefixes...
    # IT WORKS!!
    List = [[],[]]
    input_list = list(user_input)

    # Loops through all of the items in the input_list
    for item in input_list:
        # Gets item index
        item_index = input_list.index(item)
        # Checks for - as it is apart of the prefix
        if item == "-":
            # Gets the item after the -
            item_afterIndex = item_index + 1
            item_after = input_list[item_afterIndex]
            if isinstance(item_after, str):
                # Checks that it is a str, and then check if it's apart of __prefixes__
                if item_after in __prefixes__:
                        # Adds the prefix to the first part of the multidimensional list
                        List[0].append(str(item) + str(item_after))
                        # Removes prefixes from input_Lists
                        input_list.remove(item)
                        input_list.remove(item_after)
                        # Adds the rest of the input to the second part of the multidimensional list
                        for instance in input_list:
                             List[1].append(instance)
                        return List

# | ------------------------------------------------------------- | #

def input_request():
    user_input = input("Add your request: ")
    if user_input:
        __list__ = convert_string(user_input)
        return __list__
    else:
        print("Please enter a valid request.")
        input_request()
    # send info over to calculations
    # tell the main py file to not request input until it is complete with calculations

# | ------------------------------------------------------------- | #
