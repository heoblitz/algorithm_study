def AFestival(a):
    if a == 0:
        return 0
    elif a <= 1:
        return 500
    elif a <= 3:
        return 300
    elif a <= 6:
        return 200
    elif a <= 10:
        return 50
    elif a <= 15:
        return 30
    elif a <= 21:
        return 10
    else:
        return 0

def BFestival(a):
    if a == 0:
        return 0
    elif a <= 1:
        return 512
    elif a <= 3:
        return 256 
    elif a <= 7:
        return 128 
    elif a <= 15:
        return 64 
    elif a <= 31:
        return 32 
    else:
        return 0

if __name__ == '__main__':

    line = int(input())

    for _ in range(line):
        a, b = map(int, input().split())

        print((AFestival(a) + BFestival(b)) * 10000)
