def countMatches(items, ruleKey, ruleValue):
    count = 0
    for i in range(len(items)):
        if ruleKey == 'type':
            if items[i][0] == ruleValue:
                count += 1
        if ruleKey == 'color':
            if items[i][1] == ruleValue:
                count += 1
        if ruleKey == 'name':
            if items[i][2] == ruleValue:
                count += 1
    return count


if __name__ == '__main__':
    a = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],
             ["phone", "gold", "iphone"]]
    b = "color"
    c = "silver"
    print(countMatches(a,b,c))

