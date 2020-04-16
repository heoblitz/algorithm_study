int_array = list()

for _ in range(10):
    num = int(input())
    int_array.append(num % 42)

print(len(set(int_array)))