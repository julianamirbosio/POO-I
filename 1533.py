while True:
    n = int(input())
    if n == 0:
        break
    
    sus = input().split()
        
    for i in range(n):
        sus[i] = int(sus[i])
        
    sus2 = sorted(sus, reverse=True)
    suspeito = sus2[1]
    
    for i in range(n):
        if sus[i] == suspeito:
            posicao = i + 1
            
    print(posicao)
