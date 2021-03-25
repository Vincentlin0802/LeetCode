def findSpecialInteger(arr):
    dict ={}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for key in dict:
        if dict[key] > len(arr) / 4:
            return key

    """Hash = {}
    for i in arr:
        Hash[i] = Hash.get(i, 0) + 1
    for key in Hash.keys():
        if Hash[key] > len(arr) / 4:
            return key"""



if __name__ == '__main__':
    arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    print(findSpecialInteger(arr))