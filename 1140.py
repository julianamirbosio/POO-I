while True:
    frase = input().lower().split()
    
    if frase[0] == '*':
        break
    
    tautograma = True
    
    for palavra in frase:
        if palavra[0] != frase[0][0]:
            tautograma = False
            break
    
    if tautograma:
        print("Y")
    else:
        print("N")
