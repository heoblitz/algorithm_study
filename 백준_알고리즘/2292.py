num = int(input())
cnt = 1
sum = 1

while sum < num:
    sum += cnt * 6
    cnt += 1

print(cnt)