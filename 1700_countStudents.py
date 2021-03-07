def countStudents(students, sandwiches):
    times = 0
    while len(sandwiches) >0:
        if students[0] == sandwiches[0]:
            students.remove(students[0])
            sandwiches.remove(sandwiches[0])
            times = 0
        elif students[0] != sandwiches[0]:
            if times == len(students):
                return len(sandwiches)
            unlike = students[0]
            students.remove(unlike)
            students.append(unlike)
            times += 1
    return 0

if __name__ == '__main__':
    a = [1,1,1,0,0,1]
    b = [1,0,0,0,1,1]
    print(countStudents(a, b))