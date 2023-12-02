while True:
    try:
        n = int(input())
        if n == 0:
            break
        numeros = list(map(int, input().split()))
        dic = {}
        for num in numeros:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
                
        for i in dic:
            if dic[i] % 2 == 1:
                numero_solo = i
        
        print(numero_solo)
        
    except EOFError:
        break
