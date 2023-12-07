colunas = int(input())
inteiros = list(map(int, input().split()))

divisores = [2, 3, 4, 5]
linhas = len(divisores)

#criação da matriz
multiplos = [None] * linhas 
for i in range(linhas):
    multiplos[i] = [None] * colunas

#divide os inteiros pelos divisoes e imprime o resto  
for i in range(linhas):
    for j in range(colunas):
        multiplos[i][j] = (inteiros[j] % divisores[i])

#calcula os resultados
resultado = [0] * linhas       
for i in range(linhas):
    for j in range(colunas):
        if multiplos[i][j] == 0: #se o resto for 0, este inteiro é multiplo do divisor
            resultado[i] += 1
    
print("%i Multiplo(s) de 2" %(resultado[0]))
print("%i Multiplo(s) de 3" %(resultado[1]))
print("%i Multiplo(s) de 4" %(resultado[2]))
print("%i Multiplo(s) de 5" %(resultado[3]))
