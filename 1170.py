n = int(input())
for _ in range(0,n):
    c = float(input())
    d = 0
    while c > 1:
        c = c/2
        d += 1
    print("%i dias" %(d))
