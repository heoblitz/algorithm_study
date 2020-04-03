hash_dict = dict()

line = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
    hash_dict[num] = ""

line = int(input())

find_list = list(map(int, input().split()))

for find in find_list:
    if find in hash_dict:
        print("1")
    else:
        print("0")



