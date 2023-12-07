while True:
    try:
        n = int(input())
        string = []
        
        for _ in range(n):
            letra = input()
            caractere = chr(int(letra, 2))
            string.append(caractere)
            
        string = "".join(string)
        print(string)
        
    except EOFError:
        break
