n = int(input())
for _ in range(0,n): #casos teste
    soma = 0
    x, y = list(map(int, input().split()))
    x,y = min(x,y), max(x,y)
    if x % 2 == 0:
        for i in range(x+1,y,2):
            soma += i  
    elif x % 2 != 0:
        for i in range(x+2,y,2):
            soma += i  
    print(soma)
