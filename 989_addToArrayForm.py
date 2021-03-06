def addToArrayForm(A, K):
    arr =[]
    array_sum = 0
    for i in range(len(A)):
        a = A[i] * (10**(len(A)-i-1))
        array_sum = a + array_sum
    sum = K + array_sum
    str_sum = str(sum)
    for i in range(len(str_sum)):
        arr.append(int(str_sum[i]))
    return arr

if __name__ == '__main__':
    A = [2,1,5]
    K = 806
    print(addToArrayForm(A, K))
