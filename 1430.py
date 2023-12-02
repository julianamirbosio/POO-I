notas = {"W": 1, "H": 1/2, "Q": 1/4, "E": 1/8, "S": 1/16, "T": 1/32, "X": 1/64}
while True:
    try:
        jingle = input().split('/')
        if jingle[0] == '*':
            break
        else:
            compassos_corretos = 0
            for i in range(len(jingle)):
                compasso = 0
                for j in range(len(jingle[i])):
                    compasso += notas[jingle[i][j]]
                if compasso == 1:
                    compassos_corretos += 1
            print(int(compassos_corretos))
    except EOFError:
        break
