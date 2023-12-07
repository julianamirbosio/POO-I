letra = input().strip()
frase = input().split()

palavras_com_letra = 0

for palavra in frase:
    if letra in palavra:
        palavras_com_letra += 1

porcentagem = (palavras_com_letra / len(frase)) * 100  

print("%.1f" %(porcentagem))
