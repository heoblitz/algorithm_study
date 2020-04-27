weight = int(input())
cnt = 0

while weight > 0:
    if weight % 5 == 0:
        cnt += weight // 5
        weight = 0
        break
    else:
        weight -= 3
        cnt += 1

if weight == 0:
    print(cnt)
else:
    print("-1")


# 나머지가 3 이하일 때 i 를 하나 깍아도 안되는 케이스가 발생한다
# 3과 5의 최대 공배수 를 생각해봐야 할듯..