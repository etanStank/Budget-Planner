"""
    Author: Rohan
    Date: 10/02/2025
    Description: Main file for the bugdet planner.
"""

"""
    -o (One off items)
    -a (Constant income/expense over time (weekly))
    -t (Money added over time, requires a time rate, days, weeks, months, years)
    -c (Closes inout requests)
"""

# | ------------------------------------------------------------- | #

# | - Imports - | #
import src.calculations
import src.inputs
import src.outputs

# | - Globals - | #
__version__ = "0.1"

__prefixes__ = ["o", "a", "t", "c"]

src.inputs.input_request()