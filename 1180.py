n = int(input())
x = input().split()
menor = 100000
posicao = 0

for i in range(len(x)):
    x[i] = int(x[i])
    
for i in range(len(x)):
    if x[i] < menor:
        menor = x[i]
        posicao = i
print("Menor valor: %i" %(menor))
print("Posicao: %i" %(posicao))
