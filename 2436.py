l, c = list(map(int, input().split()))
a, b = list(map(int, input().split()))

chao = [None] * l 
for i in range(l):
    chao[i] = input().split()
        
ladrilhos = 0    
passos = 0
        
for i in range(l):
    for j in range(c):
        if chao[i][j] == '1':
            ladrilhos += 1
        
linha = a - 1
coluna = b - 1

while True:
    if passos == (ladrilhos - 1):
        linha += 1 
        coluna += 1 
        print(linha, coluna)
        break
    else:
        if ((coluna+1) >= 0 and (coluna+1) <= c-1) and chao[linha][coluna+1] == '1':
            chao[linha][coluna] = 'X'
            coluna += 1 
            passos += 1
        elif ((linha+1) >= 0 and (linha+1) <= l-1) and chao[linha+1][coluna] == '1':
            chao[linha][coluna] = 'X'
            linha += 1
            passos += 1
        elif ((coluna-1) >= 0 and (coluna-1) <= c-1) and chao[linha][coluna-1] == '1':
            chao[linha][coluna] = 'X'
            coluna -= 1
            passos += 1
        elif ((linha-1) >= 0 and (linha-1) <= l-1) and chao[linha-1][coluna] == '1':
            chao[linha][coluna] = 'X'
            linha -= 1
            passos += 1
        else:
            continue
