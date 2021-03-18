def findLucky(arr):
    dic = {}
    maximum = -1
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        if dic[i] == i:
            maximum = i
    return maximum



if __name__ == '__main__':
    arr = [2, 2, 3, 4]
    print(findLucky(arr))