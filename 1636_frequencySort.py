def frequencySort(nums):
    nums_count = {}
    arr = []
    for i in nums:
        if i in nums_count:
            nums_count[i] += 1
        else:
            nums_count[i] = 1
    final = sorted(nums_count.items(),key = lambda x:(x[1],-x[0]))
    for num in final:
        arr = arr + [num[0]]*num[1]
    return arr



if __name__ == '__main__':
    a = [1,1,2,2,2,3]
    print(frequencySort(a))