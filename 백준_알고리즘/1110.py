num = int(input())
answer = num
sycle = 0

while True:
    a = num // 10
    b = num % 10
    
    if a + b >= 10:
        num = (b * 10) + (a + b) % 10      
    else:
        num = (b * 10) + (a + b)
    
    sycle += 1

    if num == answer:
        print(sycle)
        break



    




