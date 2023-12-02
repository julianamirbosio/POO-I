def reprovado(alunos):
    alunos_v1 = sorted(alunos, key=lambda x: (x[0]), reverse=True)
    alunos_v2 = sorted(alunos_v1, key=lambda x: (x[1]))
    return alunos_v2[0][0]
    
k = 1
while True:
    try:
        n = int(input())
        alunos = []
        for _ in range(n):
            nome, nota = input().split()
            alunos.append((nome, int(nota)))
        print("Instancia %i" %(k))
        print(reprovado(alunos))
        print()
        k += 1
    except EOFError: 
        break
