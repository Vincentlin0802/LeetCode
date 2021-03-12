def sumOddLengthSubarrays(arr):
    sum = 0
    i = 0
    for length in range(len(arr)+1):
        if length % 2 != 0:
                for j in range(length,len(arr)+1):
                   for k in range(len(arr[i:j])):
                        sum =arr[i:j][k] + sum
                   i += 1
                i = 0
    return sum




if __name__ == '__main__':
    a = [10,11,12]
    print(sumOddLengthSubarrays(a))