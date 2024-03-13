def findPivotInteger(number):
    sums = []
    prefixSum = 0
    lastIndex = number + 1
    for i in range(0, lastIndex):
        prefixSum += i
        sums.append(prefixSum)

    totalSum = prefixSum
    for i in range(0, lastIndex):
        if i - 1 < 0:
            continue
        elif sums[i - 1] == totalSum - sums[i]:
            return i
    
    return -1
