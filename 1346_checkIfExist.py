def checkIfExist(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*2 == arr[j] or arr[j]*2 == arr[i]:
                return True
    return False

if __name__ == '__main__':
    arr = [3,1,7,11]
    print(checkIfExist(arr))