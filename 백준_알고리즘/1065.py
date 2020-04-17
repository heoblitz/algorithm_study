def solve(num):
    check = True
    diff = 0

    if num < 100:
        return check

    i = num % 10
    num //= 10
 
    temp = num % 10 # do while
    diff = i - (temp)
    num //= 10

    while num > 0:
        i = num % 10
        num //= 10

        if (temp - i) != diff:
            check = False
            return check

        temp = i

    return check

num = int(input())
cnt = 0

for i in range(1, num+1):
    if solve(i):
        cnt += 1
    
print(cnt)