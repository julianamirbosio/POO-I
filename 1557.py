while True:
    n = int(input())
    if n == 0:
        break
    else:
        matriz = [None] * n
        for i in range(n):
            matriz[i] = [None] * n
            for j in range(n):
                matriz[i][j] = 2**(i+j)
        
        for i in range(n):
            for j in range(n):
                tamanho_maior = int(len(str(matriz[n-1][n-1])))
                tamanho_menor = int(len(str(matriz[i][j])))
                matriz[i][j] = (" "*(tamanho_maior - tamanho_menor))+(str(matriz[i][j]))
            
            
        for i in range(n):
            print("%s" %(matriz[i][0]), end='')
            for j in range(1,n):
                print(" %s" % (matriz[i][j]), end='')
            print()
        print()
