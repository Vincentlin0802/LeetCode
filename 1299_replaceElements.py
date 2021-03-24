def replaceElements(arr):
    for i in range(len(arr)-1):
        arr[i] = max(arr[i + 1:])
    arr[len(arr)-1] = -1
    return arr


if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    print(replaceElements(arr))