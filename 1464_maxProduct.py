def maxProduct(nums):
    nums.sort()
    return (nums[len(nums)-1]-1) * (nums[len(nums)-2]-1)


if __name__ == '__main__':
    nums = [3,7]
    print(maxProduct(nums))