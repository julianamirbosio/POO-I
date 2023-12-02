def soma_pascal(linhas):
    if linhas == 0:
        return 0
    else:
        return 2**(linhas-1) + soma_pascal(linhas-1)
        
n = int(input())
for _ in range(n):
    linhas = int(input())
    print(soma_pascal(linhas))
