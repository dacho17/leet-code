# (digit, order) -> roman numeral
guide = {
    (1, 1): "I",
    (2, 1): "II",
    (3, 1): "III",
    (4, 1): "IV",
    (5, 1): "V",
    (6, 1): "VI",
    (7, 1): "VII",
    (8, 1): "VIII",
    (9, 1): "IX",
    (1, 2): "X",
    (2, 2): "XX",
    (3, 2): "XXX",
    (4, 2): "XL",
    (5, 2): "L",
    (6, 2): "LX",
    (7, 2): "LXX",
    (8, 2): "LXXX",
    (9, 2): "XC",
    (1, 3): "C",
    (2, 3): "CC",
    (3, 3): "CCC",
    (4, 3): "CD",
    (5, 3): "D",
    (6, 3): "DC",
    (7, 3): "DCC",
    (8, 3): "DCCC",
    (9, 3): "CM",
    (1, 4): "M",
    (2, 4): "MM",
    (3, 4): "MMM"
}

def convertIntegerToRoman(number):
    order = 1
    sol = ""
    while number != 0:
        digit = number % 10
        if digit != 0:
            romanNum = guide[(digit, order)]
            sol = romanNum + sol
        number //= 10
        order += 1
    return sol
