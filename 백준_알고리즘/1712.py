import sys

a, b , c = map(int, sys.stdin.readline().rstrip().split())

if b >= c:
    print("-1")
    exit()
else:
    cnt = a // (c - b)
    print(cnt+1)