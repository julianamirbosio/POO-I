n = int(input())

quadrado = [None] * n
for i in range(n):
    quadrado[i] = input().split()
    for j in range(n):
        quadrado[i][j] = int(quadrado[i][j])

soma_linha = []       
for i in range(n):
    soma = sum(quadrado[i])
    soma_linha.append(soma)

soma_coluna = []
transposta = [[quadrado[j][i] for j in range(n)] for i in range(n)]
for i in range(n):
    soma = sum(transposta[i])
    soma_coluna.append(soma)

soma_dif_linhas = {}
soma_dif_colunas = {}
for i in range(n):
    if not soma_linha[i] in soma_dif_linhas:
        soma_dif_linhas[soma_linha[i]] = [i]
    else:
        soma_dif_linhas[soma_linha[i]].append(i)
        
    if not soma_coluna[i] in soma_dif_colunas:
        soma_dif_colunas[soma_coluna[i]] = [i]
    else:
        soma_dif_colunas[soma_coluna[i]].append(i)    
        
somaErrada = -1
somaCorreta = -1

linhaErrada = -1
for x in soma_dif_linhas:
    if len(soma_dif_linhas[x]) == 1:
        linhaErrada = soma_dif_linhas[x][0]
        somaErrada = x
    else:
        somaCorreta = x 

colunaErrada = -1
for x in soma_dif_colunas:
    if len(soma_dif_colunas[x]) == 1:
        colunaErrada = soma_dif_colunas[x][0]
        break

valorErrado = quadrado[linhaErrada][colunaErrada]
valorOriginal = valorErrado + somaCorreta - somaErrada

print(valorOriginal, valorErrado)
