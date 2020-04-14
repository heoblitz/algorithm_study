sum = 0

for _ in range(5):
    grade = int(input())
    if grade < 40:
        grade = 40
    sum += grade

print(sum//5)