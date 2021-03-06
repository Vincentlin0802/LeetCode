def findMagicIndex(nums):
    for i in range(len(nums)):
        if nums[i] == i:
             return i
    return -1




if __name__ == '__main__':
    a = [1,1,1]
    print(findMagicIndex(a))