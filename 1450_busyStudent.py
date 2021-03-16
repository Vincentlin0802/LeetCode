def busyStudent(startTime, endTime, queryTime):
    count = 0
    j = 0
    for i in range(len(startTime)):
        if queryTime >= startTime[i] and queryTime <= endTime[j]:
            count += 1
        j+=1
    return count

if __name__ == '__main__':
    startTime = [1, 2, 3]
    endTime = [3, 2, 7]
    queryTime = 4
    print(busyStudent(startTime, endTime, queryTime))