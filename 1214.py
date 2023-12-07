c = int(input())

for i in range(c):
    n, *turma = map(int, input().split())
    media = sum(turma) / len(turma)
    acima_media = 0
    
    for i in range(len(turma)):
        if turma[i] > media:
            acima_media += 1
            
    porcentagem = acima_media / len(turma) * 100
    
    print("{:.3f}%".format(porcentagem))
