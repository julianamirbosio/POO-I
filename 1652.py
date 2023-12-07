L, N = list(map(int, input().split()))
irregulares_s = []
irregulares_p = []

for _ in range(L):
    s, p = list(map(str, input().split()))
    irregulares_s.append(s)
    irregulares_p.append(p)
    
for i in range(N):
    palavra = str(input())
    
    if palavra in irregulares_s:
        index = irregulares_s.index(palavra)
        print(irregulares_p[index])
    elif palavra.endswith("y") and not palavra.endswith("ay") and not palavra.endswith("ey") and not palavra.endswith("iy") and not palavra.endswith("oy") and not palavra.endswith("uy"):
        p = palavra[:-1] + "ies"
        print(p)
    elif palavra.endswith("o") or palavra.endswith("s") or palavra.endswith("ch") or palavra.endswith("sh") or palavra.endswith("x"):
        p = palavra + "es"
        print(p)
    else:
        p = palavra + "s"
        print(p)
