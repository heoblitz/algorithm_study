hamburger = float('inf')
drink = float('inf')

for _ in range(3):
    hamburger_price = int(input())

    if hamburger_price < hamburger:
        hamburger = hamburger_price

for _ in range(2):
    drink_price = int(input())

    if drink_price < drink:
        drink = drink_price

print((hamburger + drink) - 50)