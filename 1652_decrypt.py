def decrypt(code, k):
    sum = 0
    arr = []
    if k == 0:
        for i in range(len(code)):
            code[i] = 0
        return code
    if k > 0:
        for cur in range(len(code)):
            for j in range(cur+1,k+1):
                if j > len(code)-1:
                    for m in range(0,(k+1)-j):
                        sum = code[m] + sum
                    break
                else:
                    sum = code[j] + sum

            arr.append(sum)
            k += 1
            sum = 0
        return arr
    if k < 0:
        code.reverse()
        times = abs(k)
        for cur in range(len(code)):
            for n in range(cur+1,times+1):
                print(n)
                if n > len(code)-1:
                    for m in range(0,(times+1)-n):
                        sum = code[m] + sum
                        print(sum)
                    break
                else:
                    sum = code[n] + sum

            arr.append(sum)
            times += 1
            sum = 0
        arr.reverse()
        return arr

if __name__ == '__main__':
    a = [2,4,9,3]
    b = -2
    print(decrypt(a, b))