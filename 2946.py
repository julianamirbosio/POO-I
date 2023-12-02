def divisores(binario, lista):
    dec = int(binario, 2)
    divisores = []
    for i in lista:
        if dec % i == 0:
            divisores.append(i)
    if divisores == []:
        return "Nenhum"
    final = ' '.join(map(str, sorted(divisores)))
    return final
            
binario = input()
n = int(input())
numeros = []
for _ in range(n):
    num = int(input())
    numeros.append(num)
print(divisores(binario, numeros))
