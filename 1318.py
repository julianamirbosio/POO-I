qtdeBilhete = [None] * 10001 

while True:
    n, m = input().split()
    n = int(n)
    m = int(m)
    
    if n == 0 and m == 0:
        break
    
    bilhetesLidos = input().split()

    for i in range(1, n+1):
        qtdeBilhete[i] = 0 

    for b in bilhetesLidos:
        qtdeBilhete[int(b)] += 1

    falsos = 0
    for i in range(1, n+1):
        if qtdeBilhete[i] > 1:
            falsos += 1
    print(falsos)
