def maxContiguousN2(nums):
    numsLength = len(nums)
    maxLength = 0
    for i in range(0, numsLength):
        interSum = 0
        for j in range(i, numsLength):
            step = 1 if nums[j] == 1 else -1
            interSum += step
            if interSum == 0 and j - i + 1 > maxLength:
                maxLength = j - i + 1
    return maxLength

def maxContiguous(nums):
    numsLength = len(nums)
    maxLength, interSum = 0, 0
    interSums = { 0: -1}
    for i in range(0, numsLength):
        number = nums[i]
        step = 1 if number == 1 else -1
        interSum += step
        if interSum in interSums:
            maxLength = max(maxLength, i - interSums[interSum])
        else:
            interSums[interSum] = i
    return maxLength
