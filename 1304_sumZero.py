def sumZero(n):
    arr=[]
    if n%2 != 0:
        for i in range(-(n//2),n//2+1):
            arr.append(i)
        return arr
    if n%2 == 0:
        for j in range(-(n//2),n//2+1):
            if j == 0:
                continue
            else:
                arr.append(j)
        return arr

if __name__ == '__main__':
    n =5
    print(sumZero(n))