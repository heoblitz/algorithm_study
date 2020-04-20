a, b = map(int, input().split())
ans_a, ans_b = 0, 0
cnt = 100

while a > 0 and b > 0:
    ans_a += ( a % 10 ) * cnt
    a //= 10

    ans_b += ( b % 10 ) * cnt
    b //= 10

    cnt //= 10

print(ans_a if ans_a > ans_b else ans_b)