if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s=list(student_marks[query_name])
    s1=sum(s)
    n1=len(s)
    avg=s1/n1
    print("%.2f" % avg)
