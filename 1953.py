while True:
    try:
        chamada = {"EPR" : 0, "EHD" : 0}
        intrusos = 0
        
        n = int(input())
        for _ in range(n):
            matricula, curso = input().split()
            if curso in chamada.keys():
                chamada[curso] += 1
            else:
                intrusos += 1
                
        print("EPR: %d" %(chamada["EPR"]))
        print("EHD: %d" %(chamada["EHD"]))
        print("INTRUSOS: %d" %(intrusos))
    except EOFError:
        break
