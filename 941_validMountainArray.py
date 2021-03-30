def validMountainArray(arr):
    if len(arr) <= 2:
        return False
    if arr[0] >= arr[1]:
        return False
    pivot = 1
    for i in range(2,len(arr)):
        if pivot and arr[i-1] >= arr[i]: #下山
            pivot = 0
        if not pivot and arr[i-1] <= arr[i]:  #再次上山
            return False
    if pivot == 1:  #如果一直在上山
        return False
    else:
        return True



if __name__ == '__main__':
    arr = [3,7,6,4,3,0,1,0]
    print(validMountainArray(arr))