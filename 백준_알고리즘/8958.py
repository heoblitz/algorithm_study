line = int(input())

for _ in range(line):
    case = input()
    score = 0
    total_score = 0

    for d in case:
        if d == 'O':
            score += 1
        elif d == 'X':
            score = 0

        total_score += score
    
    print(total_score)