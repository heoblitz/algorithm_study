hash_dict = dict()
alphabet_list = [chr(i) for i in range(97, 123)]

word = list(input())

for i, w in enumerate(word):
    if w not in hash_dict:
        hash_dict[w] = i

for a in alphabet_list:
    if a in hash_dict:
        print("{0} ".format(hash_dict[a]), end='')
    else:
        print("-1 ", end='')