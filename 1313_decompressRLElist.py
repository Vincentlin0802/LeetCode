def decompressRLElist(nums):
    arr=[]
    for i in range(1,len(nums),2):
        arr += [nums[i]] * nums[i-1]
    return arr


if __name__ == '__main__':
    nums = [55,11,70,26,62,64]
    print(decompressRLElist(nums))