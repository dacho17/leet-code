def sortedSquares(nums):
    res = []
    for num in nums:
        res.append(num * num)
    res.sort()
    return res
