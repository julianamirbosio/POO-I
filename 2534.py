def exame(p, lista):
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada[p-1]

while True:
    try:
        n, q = list(map(int, input().split()))
        
        lista = []
        for _ in range(n):
            lista.append(int(input()))
        
        for _ in range(q):
            p = int(input())
            print(exame(p, lista))
            
    except EOFError:
        break
