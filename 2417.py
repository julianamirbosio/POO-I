vitorias_C, empates_C, gols_C, vitorias_F, empates_F, gols_F = input().split()

vitorias_C = int(vitorias_C)
empates_C = int(empates_C)
gols_C = int(gols_C)
vitorias_F = int(vitorias_F)
empates_F = int(empates_F)
gols_F = int(gols_F)
 
pontos_C = vitorias_C*3 + empates_C
pontos_F = vitorias_F*3 + empates_F

if pontos_C > pontos_F:
    print("C")
elif pontos_F > pontos_C:
    print("F")
else:
    if gols_C > gols_F:
        print("C")
    elif gols_F > gols_C:
        print("F")
    else:
        print("=")
