maior_numero=0
posicao=0
for i in range(1,101):
    n=int(input())
    if n > maior_numero:
        maior_numero=n
        posicao=i
print(maior_numero)
print(posicao)
