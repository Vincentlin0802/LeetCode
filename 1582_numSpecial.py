def numSpecial(mat):
    count = 0
    count2 = 0
    pivot = 0
    num = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                count += 1
                pivot = j
        if count == 1:
            for k in range(len(mat)):
                if mat[k][pivot] == 1:
                    count2 += 1
            if count2 == 1:
                num += 1
                print(num)
            count = 0
            count2 = 0
        else:
            count = 0
    return num

if __name__ == '__main__':
    a = [[0,0],
         [0,0],
         [1,0]]
    print(numSpecial(a))

