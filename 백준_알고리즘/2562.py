hash_dict = dict()
max_num = 0

for i in range(1, 10):
    num = int(input())
    hash_dict[num] = i

    if num > max_num:
        max_num = num

print("{0}\n{1}".format(max_num, hash_dict[max_num]))