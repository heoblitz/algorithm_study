weight = int(input())
cnt = 0

for i in [5, 3]:
    if weight <= 0:
        break

    current_cnt = weight // i

    if (( weight - ( current_cnt * i )) < 3 and ( weight - ( current_cnt * i )) != 0 ) :
        current_cnt -= 1
    
    weight -= current_cnt * i
    cnt += current_cnt

    print(weight, cnt, current_cnt)
    
if weight == 0:
    print(cnt)
    
else:
    print("-1")

# 나머지가 3 이하일 때 i 를 하나 깍아도 안되는 케이스가 발생한다
# 3과 5의 최대 공배수 를 생각해봐야 할듯..