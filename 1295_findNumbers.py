def findNumbers(nums):
    counter = 0
    final = 0
    for i in range(len(nums)):
        while nums[i] != 0:
            nums[i] = nums[i]//10
            counter += 1
        if counter % 2 ==0:
            final += 1
        counter = 0
    return final

if __name__ == '__main__':
    nums = [12,345,2,6,7896]
    print(findNumbers(nums))