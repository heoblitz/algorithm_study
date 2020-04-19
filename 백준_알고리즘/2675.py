line = int(input())

for _ in range(line):
    i, word = input().split()
    i = int(i)

    for d in word:
        print(d * i, end='')
    print("")