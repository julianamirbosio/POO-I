lista = []
comportadas = 0
n_comportadas = 0

def ordem_alfabetica(lista_nomes):
    nomes_ordenados = sorted(lista_nomes)
    return nomes_ordenados
    
n = int(input())
for _ in range(n):
    comportamento, nome = input().split()
    lista.append(nome)
    if comportamento == '+':
        comportadas += 1
    else: 
        n_comportadas += 1

criancas_az = ordem_alfabetica(lista)

for menine in criancas_az:
    print(menine)
print("Se comportaram: %d | Nao se comportaram: %d" %(comportadas, n_comportadas))
