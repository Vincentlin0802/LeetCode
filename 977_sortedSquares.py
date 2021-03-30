def sortedSquares(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    nums.sort()
    return nums


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums))