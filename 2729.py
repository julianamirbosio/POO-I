def ordem(lista):
    return sorted(set(lista))
    
n = int(input())
for _ in range(n):
    lista = input().split()
    print(" ".join(ordem(lista)))
