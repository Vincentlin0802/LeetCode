def largestAltitude(gain):
    arr= [0]
    for i in range(len(gain)):
        arr.append(gain[i]+arr[i])
    return max(arr)



if __name__ == '__main__':
    a =[-4,-3,-2,-1,4,3,2]
    print(largestAltitude(a))