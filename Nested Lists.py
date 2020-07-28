if __name__ == '__main__':
    students=list()
    temp_ls=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp_ls=(score,name)
        students.append(temp_ls)
    students.sort()
    count=0
    min1=students[0][0]
    for i in range(len(students)):
        if min1==students[i][0]:
            count=count+1
    if count>=1:
        for j in range(count):
            students.pop(0)
    min2=students[0][0]
    for i in range(len(students)):
        if min2==students[i][0]:
            print(students[i][1])
