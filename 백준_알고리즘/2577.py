cnt_list = [0 for x in range(10)]
mul = 1

for _ in range(3):
    num = int(input())
    mul *= num

for i in map(int, str(mul)):
    cnt = cnt_list[i]
    cnt_list[i] = cnt + 1

print('\n'.join(map(str, cnt_list)))