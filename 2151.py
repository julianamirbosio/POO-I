c = int(input())

for k in range(1,c+1):
    
    m, n, x, y = list(map(int, input().split()))
    x = x - 1
    y = y - 1
    
    parede = [None] * m
    for i in range(m):
        parede[i] = input().split()
        for j in range(n):
            parede[i][j] = int(parede[i][j])
    
    for i in range(m):
        for j in range(n):
            distancia = max(abs(i-x),abs(j-y))
            if distancia > 8:
                parede[i][j] += 1
            else:
                parede[i][j] += 10 - distancia 
                
    print("Parede %i:" % (k))
    for i in range(m):
        print("%s" % (parede[i][0]), end='')
        for j in range(1,n):
            print(" %s" % (parede[i][j]), end='')
        print()
