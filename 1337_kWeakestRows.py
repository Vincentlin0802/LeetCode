def kWeakestRows(mat, k):
    dict = {}
    sum = 0
    arr = []
    for i in range(len(mat)):
        if i not in dict:
            for j in range(len(mat[0])):
                sum = sum +mat[i][j]
            dict[i] = (sum)
            sum = 0
    order = sorted(dict.items(),key =lambda x:x[1],reverse = False)
    print(order)
    for num in order:
        arr = arr + [num[0]]
    return arr[:k]

if __name__ == '__main__':
    mat =[[1,0],[1,0],[1,0],[1,1]]
    k = 4
    print(kWeakestRows(mat, k))

