c = int(input())
for _ in range(c):
    cod = str(input().strip())
    cod = cod[::-1]
    mensagem = ""
    for minuscula in cod:
        if not minuscula.isupper():
            mensagem += minuscula
    print(mensagem)
