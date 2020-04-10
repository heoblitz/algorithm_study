hour, minute = map(int, input().split())

if minute - 45 >= 0:
    print(hour, minute - 45)
else:
    if hour - 1 >= 0:
        print(hour - 1, minute + 15)
    else:
        print(hour + 23, minute + 15)
