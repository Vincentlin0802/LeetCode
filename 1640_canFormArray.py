def canFormArray(arr, pieces):
    i = 0
    while(i<len(arr)):
        counter = 0
        for j in range(i+1,len(arr)+1):
            if arr[i:j] in pieces:
                counter = 1
                break
        if counter == 0:
            return False
        else:
            i = j
    return True






if __name__ == '__main__':
    a = [49,18,16]
    b = [[16,18,49]]
    print(canFormArray(a, b))