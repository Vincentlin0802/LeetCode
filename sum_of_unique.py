def sumOfUnique(nums):
    arr = set(nums)
    total_sum = 0
    for i in arr:
        if nums.count(i) == 1:
           total_sum = i + total_sum
    return total_sum






if __name__ == '__main__':
    a = [1,1,1,1,1]
    print(sumOfUnique(a))