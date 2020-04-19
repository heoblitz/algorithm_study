hash_dict = {chr(x): 0 for x in range(65, 91)}
word = input()
cnt = 0

for d in word.upper():
    cnt = hash_dict[d]
    cnt += 1

    hash_dict[d] = cnt

cnt_list = list(hash_dict.values())
cnt_list.sort(reverse=True)

if cnt_list[0] != cnt_list[1]:
    max_key = max(hash_dict, key=hash_dict.get)
    print(max_key)
else:
    print("?")