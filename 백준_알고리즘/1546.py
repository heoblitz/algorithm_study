cnt = int(input())
grade_list = list(map(int, input().split()))
sum = 0

grade_list.sort()
high_grade = grade_list[-1]

for grade in grade_list:
    sum += ((grade / high_grade) * 100)

print(sum/cnt)