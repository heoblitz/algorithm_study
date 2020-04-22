line = int(input())
hash_dict = {}
cnt = 0

for _ in range(line):
    word = input()
    check = True

    for w in word:
        if w not in hash_dict:
            hash_dict[w] = True
        else:
            if temp != w:
                check = False
                break
        temp = w
        
    hash_dict = {}

    if check:
        cnt += 1

print(cnt)