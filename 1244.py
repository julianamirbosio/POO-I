def organizacao_por_tamanho(lista):
    return sorted(lista, key=len, reverse=True)
    
n = int(input())
for _ in range(n):
    frase = input().split()
    print(" ".join(organizacao_por_tamanho(frase)))
