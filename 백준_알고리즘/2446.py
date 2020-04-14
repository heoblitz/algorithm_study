line = int(input())
width = (line*2) - 1

for i in range(width, 0, -2):
    print(" " * ((width - i) // 2), end='')
    print("*" * i)

for j in range(3, width+1, 2):
    print(" " * ((width - j) // 2), end='')
    print("*" * j)