def maximumOddBinary(binaryNumber):
    numberOfZeroes = 0
    lengthOfNumber = 0
    for digit in binaryNumber:
        if digit == '0':
            numberOfZeroes += 1
        lengthOfNumber += 1
    
    largestOddBinaryNumber = "1"
    for i in range(0, numberOfZeroes):
        largestOddBinaryNumber = "0" + largestOddBinaryNumber
    for i in range(0, lengthOfNumber - numberOfZeroes - 1):
        largestOddBinaryNumber = "1" + largestOddBinaryNumber
    
    return largestOddBinaryNumber
