import sys

line = int(sys.stdin.readline().rstrip())

for _ in range(line):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)
