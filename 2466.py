n = int(input())
fileira = input().split()

triangulo = [fileira]

for i in range(n-1):
    linha = []
    for j in range(len(triangulo[i]) - 1):
        if triangulo[i][j] == triangulo[i][j+1]:
            linha.append('1')
        else:
            linha.append('-1')
    triangulo.append(linha)
            
if triangulo[n-1][0] == '-1':
    print("branca")
else:
    print("preta")
