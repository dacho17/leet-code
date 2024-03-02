def reverseInteger(number):
    prefixSign = 1 if number >= 0 else - 1
    number = number * prefixSign    # make the integer positive if it is negative

    stack = getStackedDigits(number)
    res = 0
    order = 0
    for digit in stack:
        res += digit * 10 ** order
        order += 1
    return res * prefixSign

def getStackedDigits(number):
    stack = []
    isLeadingDigit = True
    while number != 0:
        digit = number % 10
        number //= 10
        if isLeadingDigit and digit == 0:
            continue

        isLeadingDigit = False
        stack.insert(0, digit)
    return stack
