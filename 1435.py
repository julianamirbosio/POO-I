matriz = [None] * 100
for i in range(100):
    matriz[i] = [None] * 100

while True:
    n = int(input())
    if n == 0:
        break
	
    if n % 2 == 0:
	    t = n // 2
    else:
	    t = 1 + n // 2
	
    min = 0
    max = n 
    cont = 0
	
    for k in range(0, t):
        cont += 1
        for i in range(min, max):
            for j in range(min, max):
                matriz[i][j] = cont
        min += 1 
        max -= 1 
        
    for i in range(n):
        print("%3d" % matriz[i][j], end='')
        for j in range(1, n):
            print(" %3d" % matriz[i][j], end='')
        print()
    print()
