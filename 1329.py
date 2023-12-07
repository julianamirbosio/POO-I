while True:
    mary = 0
    john = 0
    
    n = int(input())
    if n == 0:
        break
    
    jogos = input().split()
        
    for i in range(len(jogos)):
        if jogos[i] == '0':
            mary += 1
        elif jogos[i] == '1':
            john += 1
            
    print("Mary won %d times and John won %d times" % (mary, john))
