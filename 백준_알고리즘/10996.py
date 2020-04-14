line = int(input())

for i in range(line):
    x = line // 2
    y = line - x
    print("* " * y)
    print(" *" * x)