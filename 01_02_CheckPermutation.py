def CheckPermutation(s1, s2):
    pivot =0
    arr1 = list(s1)
    arr2 = list(s2)
    if len(s1) != len(s2):
        return False
    for i in range(len(arr1)):
        for j in range(pivot,len(arr2)):
            if arr1[i] == arr2[j]:
                arr2[j],arr2[i] = arr2[i],arr2[j]
                pivot += 1
                break
            elif arr1[i] != arr2[j] and j == len(arr2)-1:
                return False
    return True

if __name__ == '__main__':
    a = "abc"
    b = "bca"
    print(CheckPermutation(a, b))
