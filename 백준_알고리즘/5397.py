import sys

line = int(sys.stdin.readline())

answer_list = list()

for _ in range(line):
    answer = list()
    temp = list()
    passwd = sys.stdin.readline().strip()

    for key in passwd:

        if key == '<':
            if answer:
                temp.append(answer.pop())
        
        elif key == '>':
            if temp:
                answer.append(temp.pop())

        elif key == '-':
            if answer:
                answer.pop()

        else:
            answer.append(key)


    answer.extend(reversed(temp))
    print(''.join(answer))

