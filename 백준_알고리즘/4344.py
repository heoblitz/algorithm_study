line = int(input())

for _ in range(line):
    grade_list = list(map(int, input().split()))
    cnt = grade_list.pop(0)

    over_cnt = 0
    sum = 0
    average = 0

    for grade in grade_list:
        sum += grade
    
    average = sum / cnt

    for grade in grade_list:
        if grade > average:
            over_cnt += 1

    print("{0:.3f}%".format((over_cnt/cnt) * 100))