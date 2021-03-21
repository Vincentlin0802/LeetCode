def createTargetArray(nums, index):
    target = []
    for i in range(len(nums)):
        target.insert(index[i],nums[i])
    return target

if __name__ == '__main__':
    nums = [1]
    index = [0]
    print(createTargetArray(nums, index))