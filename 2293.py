n, m = list(map(int, input().split()))

fazenda = [None] * n
for i in range(n):
    fazenda[i] = input().split()
    for j in range(m):
        fazenda[i][j] = int(fazenda[i][j])
        
maior_linha = 0
for linha in fazenda:
    if sum(linha) > maior_linha:
        maior_linha = sum(linha)
        
maior_coluna = 0
fazenda_transposta = list(zip(*fazenda))
for coluna in fazenda_transposta:
    if sum(coluna) > maior_coluna:
        maior_coluna = sum(coluna)
        
print(max(maior_linha, maior_coluna))
