n = int(input())
sociedade = {'A' : 0, 'E' : 0, 'H' : 0, 'M' : 0, 'X' : 0}
for _ in range(n): 
    nome, raca = input().split()
    if raca in sociedade:
        sociedade[raca] += 1
        
print("%d Hobbit(s)" % sociedade['X'])
print("%d Humano(s)" % sociedade['H'])
print("%d Elfo(s)" % sociedade['E'])
print("%d Anao(oes)" % sociedade['A'])
print("%d Mago(s)" % sociedade['M'])
