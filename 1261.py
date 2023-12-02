m, n = list(map(int, input().split()))

trabalho = {}
for _ in range(m):
    cargo, remuneracao = input().split()
    remuneracao = int(remuneracao)
    trabalho[cargo] = remuneracao

for _ in range(n):
    descricao = []
    while True:
        linha = input()
        if linha == ".":
            break
        descricao.extend(linha.split())
    
    PontosDeFeno = 0
    for palavra in descricao:
        if palavra in trabalho:
            PontosDeFeno += trabalho[palavra]
    
    print(PontosDeFeno)
