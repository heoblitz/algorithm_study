def solve(c):
    if c >= 'A' and c <= 'C':
        return 3
    elif c >= 'D' and c <= 'F':
        return 4
    elif c >= 'G' and c <= 'I':
        return 5
    elif c >= 'J' and c <= 'L':
        return 6
    elif c >= 'M' and c <= 'O':
        return 7
    elif c >= 'P' and c <= 'S':
        return 8
    elif c >= 'T' and c <= 'V':
        return 9
    elif c >= 'W' and c <= 'Z':
        return 10

code = input()
time = 0

for c in code:
    time += solve(c)

print(time)