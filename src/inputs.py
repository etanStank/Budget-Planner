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

# | ------------------------------------------------------------- | #

def convert_string(user_input):
    # Converts the initial input into a multidimensional list which seperates the prefix from the request.
    # Doesn't check edge cases but eh, should check for all prefixes...
    List = [[],[]]
    input_list = list(user_input)
    print(input_list)

    print("HERRO 2")
    for item in input_list:
        item_index = input_list.index(item)
        if item == "-":
            print("HERRO 123")
            print(f"Item Index: {item_index}")
            item_afterIndex = item_index + 1
            item_after = List[item_afterIndex]
            print(f"Item after: {item_after}")
            if isinstance(item_after, str):
                print("ASD")
                if item_after in __prefixes__:
                        print("HERRO 3")
                        List[0].append(str(item) + str(item_after))
    return List

# | ------------------------------------------------------------- | #

def input_request():
    user_input = input("Add your request: ")
    if user_input:
        convert_string(user_input)
        print("HERRO")
    else:
        print("Please enter a valid request.")
        input_request()
    # send info over to calculations
    # tell the main py file to not request input until it is complete with calculations

# | ------------------------------------------------------------- | #

print(input_request())
