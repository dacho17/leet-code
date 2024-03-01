def twoSum(nums, target):
    summands = {}
    index = 0
    for num in nums:
        if num in summands:
            return [summands[num], index]
        else:
            missingSummand = target - num
            summands[missingSummand] = index
            index += 1
    return [-1, -1]
