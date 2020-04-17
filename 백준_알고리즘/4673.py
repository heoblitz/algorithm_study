def solve(i):
    self_number = 0
    num = i

    while i > 0:
        self_number += i % 10
        i //= 10

    self_number += num

    return self_number

def solve_print(ans_list):
    for i, b in enumerate(ans_list):
        if i == 0:
            continue
        if b == False:
            print(i)

ans_list = [False for i in range(10001)]
self_number = 0
index = 1

for index in range(1, 10001):
    self_number = solve(index)

    if self_number > 10000:
        continue
    else:
        ans_list[self_number] = True

    index += 1

solve_print(ans_list)