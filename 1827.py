while True:
    try:
        n = int(input())
        
        matriz = [0] * n
        for i in range(n):
            matriz[i] = [0] * n
            
        for i in range(n):
            for j in range(n):
                
                if i == j:
                    matriz[i][j] = '2'
                    
                matriz[i][n-i-1] = '3'
        
        t = (n//3)         
        for i in range(t, n-t):
            for j in range(t, n-t):    
                matriz[i][j] = '1'
        
        for i in range(n):
            for j in range(n):
                matriz[n//2][n//2] = '4'
                
        for i in range(n):
            for j in range(n):
                print("%s" % (matriz[i][j]), end='')
            print()
        print()
                
    except EOFError:
        break
