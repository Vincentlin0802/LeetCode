def specialArray(nums):
    count = 0
    for x in range(len(nums)+1):
        for i in range(len(nums)):
            if nums[i] >= x:
                count += 1
        if count == x:
            return x
        else:
            count = 0
    return -1


if __name__ == '__main__':
    a = [0,4,3,0,4]
    print(specialArray(a))