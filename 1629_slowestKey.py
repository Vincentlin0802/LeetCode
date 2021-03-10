def slowestKey(releaseTimes, keysPressed):
    arr = {}
    for i in range (len(keysPressed)):
        if i == 0:
            arr[keysPressed[i]] = releaseTimes[i]
        else:
            if keysPressed[i] in arr:
                if releaseTimes[i] - releaseTimes[i-1] > arr.get(keysPressed[i]):
                    arr[keysPressed[i]] = releaseTimes[i] - releaseTimes[i-1]
            else:
                 arr[keysPressed[i]] = releaseTimes[i] - releaseTimes[i - 1]
    arr = sorted(arr.items(),key = lambda item:item[1])
    max_times =  arr[len(arr)-1][1]
    max_keys = arr[len(arr)-1][0]
    for j in range(len(arr)-2,0,-1):
        if arr[j][1] == max_times:
            if arr[j][0] > arr[len(arr)-1][0]:
                max_keys = arr[j][0]
    return max_keys



if __name__ == '__main__':
    a = [9,29,49,50]

    b = "cbcd"
    print(slowestKey(a, b))