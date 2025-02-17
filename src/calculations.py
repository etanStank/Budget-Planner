"""
    Author: Rohan
    Date: 10/02/2025
    Description: Responsible for all of the calculations relating to any math.
"""

# | ------------------------------------------------------------- | #

__prefixes__ = ["o", "a", "t", "c"]

items = []
costs = []
time = []

# | ------------------------------------------------------------- | #

def findMoneyInterger(moneyList):
    # Finds the money from the list
    money_value = 0
    for item in moneyList:
        if item == "$":
            currency_symbol_index = moneyList.index(item)
            for number in range(currency_symbol_index, len(moneyList)):
                if moneyList[number].isdigit():
                    money_value = moneyList[int(number)] + int(money_value)
                    continue
                else:
                    continue
   
    return money_value
# | ------------------------------------------------------------- | #
def calculate(__list__):
    prefix = __list__[0]
    data = __list__[1]

    
print(findMoneyInterger(["$", "1", "0", "0", "0"]))