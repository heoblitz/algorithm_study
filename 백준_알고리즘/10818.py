line = int(input())
int_array = list(map(int, input().split()))
int_array.sort()

print(int_array[0], int_array[-1])