teste = 1 
while True:
    a, v = list(map(int, input().split()))
    if a == 0 and v == 0:
        break
    
    aeroporto = [0] * (a+1)
    
    for i in range(v):
        x, y = list(map(int,input().split()))
        aeroporto[x] += 1 
        aeroporto[y] += 1
        
    maior = 0
    for i in range(len(aeroporto)):
        if aeroporto[i] > maior:
            maior = aeroporto[i]
    
    
    print("Teste %i" %(teste))
    
    primeiro = True
    for i in range(len(aeroporto)):
        if maior == aeroporto[i]:
            print("%i "%(i),end='')
            '''if primeiro:
                print("%i"%(i),end='')
                primeiro = False
            else:
                print(" %i"%(i),end='')'''
    print()
    print()
    teste += 1
