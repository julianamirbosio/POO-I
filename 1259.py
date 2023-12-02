def paridade(lista):
    pares = [x for x in lista if x % 2 == 0]
    impares = [x for x in lista if x % 2 != 0]
    
    pares = sorted(pares)
    impares = sorted(impares, reverse=True)
    return pares + impares
    
n = int(input())
valores = []
for i in range(n):
    num = int(input())
    valores.append(num)

resultado = paridade(valores)
for i in range(n):
    print(resultado[i])
