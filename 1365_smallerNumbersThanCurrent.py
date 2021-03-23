def smallerNumbersThanCurrent(nums):
    times = []
    counter = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] > nums[j] and i != j:
                counter += 1
        times.append(counter)
        counter = 0
    return times


if __name__ == '__main__':
    nums = [6,5,4,8]
    print(smallerNumbersThanCurrent(nums))