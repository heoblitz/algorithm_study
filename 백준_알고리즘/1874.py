import sys

data_list = list(map(int, sys.stdin.readlines()))
stack_list = list()
result_list = list()

data_list.pop(0)

value = 1
stack_list.append(value)

for data in data_list:
    while data >= value:
        stack_list.append(value)
        value += 1
        result_list.append("+")

    if data == stack_list[-1]:
        stack_list.pop()
        result_list.append("-")

    else:
        print("NO")
        exit(0)

print('\n'.join(result_list))
