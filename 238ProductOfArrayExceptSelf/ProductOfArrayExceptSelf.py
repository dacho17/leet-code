def getProducts(nums):
    leftProduct = 1
    products = []
    for num in nums:
        products.append(leftProduct)
        leftProduct *= num

    rightProduct = 1
    lenNums = len(nums) - 1
    for i in range(lenNums, -1, -1):
        products[i] *= rightProduct
        rightProduct *= nums[i]
    return products
