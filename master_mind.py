def masterMind(solution, guess):
    hashmap = {'R':0,'G':0,'B':0,'Y':0}
    hashmap1 = {'R':0,'G':0,'B':0,'Y':0}
    arr =[]
    guess_half = 0
    for i in range(4):
        if guess[i] != solution[i]:
            arr.append(i)
    for i in arr:
        hashmap[solution[i]] += 1
        hashmap1[guess[i]] += 1
    value = list(hashmap.values())
    value1 = list(hashmap1.values())
    for i in range(4):
        if value[i] > 0 and value1[i] > 0:
            guess_half += min(value[i],value1[i])
    return(4-len(arr),guess_half)



if __name__ == '__main__':
    a = "YYRG"
    b = "RRRR"
    print(masterMind(a, b))