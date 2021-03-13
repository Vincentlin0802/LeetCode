def numIdenticalPairs(nums):
    counter = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i<j:
                counter += 1
    return counter



if __name__ == '__main__':
    nums = [1,2,3]
    print(numIdenticalPairs(nums))

