n, x = map(int, input().split())
int_array = list(map(int, input().split()))

for i in int_array:
    if i < x:
        print("{0} ".format(i), end="")
