def kidsWithCandies(candies, extraCandies):
    arr =[]
    for i in range(len(candies)):
        arr.append(candies[i]+extraCandies >= max(candies))
    return arr

if __name__ == '__main__':
    candies = [12,1,12]
    extraCandies = 10
    print(kidsWithCandies(candies, extraCandies))