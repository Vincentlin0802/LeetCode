def canMakeArithmeticProgression(arr):
     arr.sort()
     difference = arr[1] - arr[0]
     for i in range(2,len(arr)):
         if arr[i] - arr[i-1] == difference:
             continue
         else:
            return False
     return True









if __name__ =='__main__':
    a = [3,5,1]
    print(canMakeArithmeticProgression(a))