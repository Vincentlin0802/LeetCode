def findKthPositive(arr, k):
    lost_arr = []
    j = 1
    for i in range(1,arr[len(arr)-1]):
        if i not in arr:
            lost_arr.append(i)
            print(lost_arr)
        if len(lost_arr) == k:
            return lost_arr[k-1]
    while len(lost_arr) != k:
        lost_arr.append(arr[len(arr)-1]+j)
        j += 1
    return lost_arr[k-1]

if __name__ == '__main__':
    a = [1,2,3,4]
    b = 2
    print(findKthPositive(a, b))