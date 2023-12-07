n = int(input())
for _ in range(n):
    painel = input()
    leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    total = 0
    for digito in painel:
        x = int(digito)
        total += leds[x]
    print("%i leds" %(total))
