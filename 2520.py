while True:
    try:
        n, m = list(map(int, input().split()))
        
        cidade = [None] * n
        for i in range(n):
            cidade[i] = input().split()
            
        for i in range(n):
            for j in range(m):
                if cidade[i][j] == '2':
                    xa = j
                    ya = i
                if cidade[i][j] == '1':
                    xj = j
                    yj = i
                    
        distancia_x = (xa - xj)
        if distancia_x < 0:
            distancia_x = -1 * (distancia_x)
            
        distancia_y = (ya - yj)
        if distancia_y < 0:
            distancia_y = -1 * (distancia_y)
            
        print(distancia_x+distancia_y)
        
    except EOFError:
        break
