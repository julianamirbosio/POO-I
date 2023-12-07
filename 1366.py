while True:
    n = int(input())
    if n == 0:
        break
    qtdPares = 0
    for i in range(n):
        c, v = list(map(int, input().split()))
        
        qtdPares += (v//2)
    
    print(qtdPares//2)
