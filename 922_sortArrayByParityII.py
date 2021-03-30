def sortArrayByParityII(nums):
    odd = []
    even = []
    for i in range(len(nums)):
        if nums[i] % 2 ==0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    m = 0
    n = 0
    for j in range(len(nums)):
        if j % 2 ==0:
            nums[j] = even[m]
            m += 1
        else:
            nums[j] = odd[n]
            n += 1
    return nums