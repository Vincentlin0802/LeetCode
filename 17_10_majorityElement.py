def majorityElement(nums):
    arr = set(nums)
    for i in arr:
        if nums.count(i) > (len(nums)/2):
            return i
    return -1




if __name__ == '__main__':
    a = [2,2,1,1,1,2,2]
    print(majorityElement(a))