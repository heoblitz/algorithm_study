a, b, v = map(int, input().split())

day = (v-a) // (a - b)
lost = (v-a) % (a - b)

if lost != 0:
    print(day+2)
else:
    print(day+1)