guide = {
    "I": (1, 1),
    "V": (5, 2),
    "X": (10, 3),
    "L": (50, 4),
    "C": (100, 5),
    "D": (500, 6),
    "M": (1000, 7)
}

def transformRomanToDecimal(roman):
    curOrder, sol = 0, 0
    for i in range(len(roman) - 1, -1, -1):
        value, order = guide[roman[i]]
        sol += -value if order < curOrder else value
        curOrder = max(order, curOrder)
    return sol
