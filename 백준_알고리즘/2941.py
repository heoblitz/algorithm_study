buff = list()
lang_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for lang in lang_list:
    word = word.replace(lang, "*")

print(len(word))