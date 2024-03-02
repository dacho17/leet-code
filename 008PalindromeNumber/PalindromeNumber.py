def isPalindrome(number):
    if number < 0:
        return False
    
    numberLength = getNumberLength(number)
    halfPoint = numberLength // 2
    hasOddDigits = numberLength % 2 == 1
    curIndex = 0
    stack = []
    while curIndex < numberLength:
        digit = number % 10
        number //= 10
        
        if hasOddDigits and curIndex == halfPoint:  # we are on half point of the number with odd amount of digits
            pass
        elif curIndex < halfPoint:  # we are adding prefix digits to stack
            stack.insert(0, digit)
        else:   # we are checking if sufix matches the prefix digit
            prefixDigit = stack.pop(0)
            if digit != prefixDigit:
                return False
        curIndex += 1
    return True

def getNumberLength(number):
    if number == 0:
        return 1

    sol = 0
    while number != 0:
        number //= 10
        sol += 1
    return sol
