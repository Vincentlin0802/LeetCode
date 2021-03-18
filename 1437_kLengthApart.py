def kLengthApart(nums, k):
    arr = []
    for i in range(len(nums)):
        if nums[i] == 1:
            arr.append(i)
    for j in range(1,len(arr)):
        if arr[j] -arr[j-1]-1<k:
            return False
    return True


if __name__ == '__main__':
    nums =[1,0,0,0,1,0,0,0,0,0,0,0,1,0,1]
    k = 2
    print(kLengthApart(nums, k))

