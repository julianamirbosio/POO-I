while True:
    try:
        n, m = list(map(int, input().split()))
        
        mat = [None] * n
        for i in range(n):
            mat[i] = input().split()
        
        tabuleiro = [None] * n
        for i in range(n):
            tabuleiro[i] = [0] * m
            
        for i in range(n):
            for j in range(m):
                if mat[i][j] == '1':
                    tabuleiro[i][j] = 9
                else:
                    
                    i_vizinho = i - 1
                    j_vizinho = j
                    if i_vizinho >= 0 and mat[i_vizinho][j_vizinho] == '1':
                        tabuleiro[i][j] += 1
                        
                    i_vizinho = i + 1
                    j_vizinho = j
                    if i_vizinho < n and mat[i_vizinho][j_vizinho] == '1':
                        tabuleiro[i][j] += 1
                        
                    i_vizinho = i
                    j_vizinho = j - 1
                    if j_vizinho >= 0 and mat[i_vizinho][j_vizinho] == '1':
                        tabuleiro[i][j] += 1
                        
                    i_vizinho = i
                    j_vizinho = j + 1
                    if j_vizinho < m and mat[i_vizinho][j_vizinho] == '1':
                        tabuleiro[i][j] += 1
                        
        for i in range(n):
            for j in range(m):
                print("%d" % (tabuleiro[i][j]), end='')
            print()
        
    except EOFError:
        break
