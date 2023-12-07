solucoesProblemas = [None] * 101
while True:
    n, m = list(map(int, input().split()))
    if n == 0 and m == 0:
        break
        
    for i in range(m):
        solucoesProblemas[i] = 0 #Anoto a quantidade de times que resolveu cada problema, inicialmente com 0


    #Marco todos os critérios como verdadeiros até que depois consiga marcar algum como falso
    ngnResolveuTodos = True
    aoMenosUmProblema = True
    todoProblemaResolvido = True
    naoResolvidoPorTodos = True
    
    for i in range(n):
        solucoes = input().split()
        
        qtdeResolvidosTime = 0
        for j in range(m):
            if solucoes[j] == '1':
                qtdeResolvidosTime += 1 #Aumento a quantidade de problemas resolvidos pelo time i
                solucoesProblemas[j] += 1 #Aumento a quantidade de soluções para o problema j
        
        if qtdeResolvidosTime == m: #Se a quantidade de problemas resolvidos pelo time for igual ao total de problemas
            ngnResolveuTodos = False
            
        if qtdeResolvidosTime == 0: #Se o time não resolveu nada
            aoMenosUmProblema = False
    

    for i in range(m):
        if solucoesProblemas[i] == 0: #Se ninguém resolveu o problema i
            todoProblemaResolvido = False
        if solucoesProblemas[i] == n: #Se todos resolveram o problema i
            naoResolvidoPorTodos = False
    
    #Apenas somo 1 a cada critério satisfeito
    criteriosSatisfeitos = 0
    if ngnResolveuTodos:
        criteriosSatisfeitos += 1
    if aoMenosUmProblema:
        criteriosSatisfeitos += 1
    if todoProblemaResolvido:
        criteriosSatisfeitos += 1
    if naoResolvidoPorTodos:
        criteriosSatisfeitos += 1
    
    print(criteriosSatisfeitos)
