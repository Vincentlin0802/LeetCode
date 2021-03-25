def minCostToMoveChips(position):
    odd, even = 0,0
    for i in position:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return min(odd,even)

if __name__ == '__main__':
    chips = [1,2,3]
    print(minCostToMoveChips(chips))