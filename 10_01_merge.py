def merge(A, m, B, n):
    cur = n - 1
    ptr = m -1
    ptr2 = len(A) - 1
    while cur >= 0:
        if ptr < 0:
            A[0:cur+1] = B[0:cur+1]
            break
        elif A[ptr] > B[cur]:
            A[ptr2] = A[ptr]
            ptr -= 1
        else:
            A[ptr2] = B[cur]
            cur -= 1
        ptr2 -= 1
    return A


if __name__ == '__main__':
    a = [4,0,0,0,0,0]
    c = 1
    b = [1,2,3,5,6]
    d = 5
    print(merge(a, c, b, d))