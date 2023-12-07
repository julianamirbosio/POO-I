o = input()

mat = [None] * 12
for linha in range(0, 12):
    mat[linha] = [None] * 12
    
for i in range(0, 12):
    for j in range(0, 12):
        mat[i][j] = float(input())
        
soma = 0
for i in range(0, 12):
    for j in range(0, (12 - (i+1))):
        soma += mat[i][j]
        
qtde = (144 - 12) / 2        
if o == 'S':
    print("%.1f" % (soma))
else:
    print("%.1f" % (soma / qtde))
