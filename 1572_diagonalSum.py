def diagonalSum(mat):
    tr = 0
    tc = 0
    dr = len(mat)-1
    dc = len(mat)-1
    sum = 0
    if len(mat) == 1:
        return mat[0][0]
    for i in range(len(mat)//2):
        sum = mat[tr+i][tc+i] + mat[tr+i][dc-i] + mat[dr-i][tr+i] +mat[dr-i][dc-i] + sum
    if len(mat)%2 != 0:
        sum = sum + mat[len(mat)//2][len(mat)//2]
    return sum

if __name__ == '__main__':
    a = [[7,3,1,9],
         [3,4,6,9],
         [6,9,6,6],
         [9,5,8,5]]
    print(diagonalSum(a))