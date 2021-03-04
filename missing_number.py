def missingNumber(nums):
    odd = 0
    even = 0
    a = len(nums)
    if len(nums) % 2 != 0:
        for i in range(a):
            if nums[i] % 2 == 0:
                even += 1
            else:
                odd += 1
        if odd > even:
            for j in range(a+1):
                if j % 2 == 0 and j not in nums:
                    return j
        else:
            for j in range(a+1):
                if j % 2 != 0 and j not in nums:
                    return j
    elif len(nums) % 2 == 0:
        for i in range(a):
            if nums[i] % 2 == 0:
                even += 1
            else:
                odd += 1
    if odd == even:
        for j in range(a + 1):
            if j % 2 == 0 and j not in nums:
                return j
    elif even - odd > 1:
        for j in range(a + 1):
            if j % 2 != 0 and j not in nums:
                return j



if __name__ == '__main__':
    a = [0,1]
    print(missingNumber(a))

