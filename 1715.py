n, m = list(map(int, input().split()))

matriz = [None] * n
for i in range(n):
    matriz[i] = input().split()
      
nao_craque = 0
for i in range(n):
    if '0' in matriz[i]: 
        nao_craque += 1

print(n - nao_craque)
