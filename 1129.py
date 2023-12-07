r = 'ABCDE*'    
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(0,n):
        p = -1
        L = [int(x) for x in input().split()]
        for j in range(0,len(L)):
            if L[j] <= 127:
                if p != -1:
                    p = 5
                    break
                p = j 
        print(r[p])
