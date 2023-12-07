celulas = int(input())
campoMinado = [0, 0, 0]

for i in range(celulas + 1):
    if i < celulas:
        campoMinado[i % 3] = int(input())
    else:
        campoMinado[i % 3] = 0

    if i > 0:
        print(campoMinado[0] + campoMinado[1] + campoMinado[2])
