n = int(input())
traducao = {}
for _ in range(n):
    lingua = input()
    traducao[lingua] = input() 

m = int(input())
for _ in range(m):
    nome = input()
    idioma = input()
    print(nome)
    print(traducao[idioma])
    print()
