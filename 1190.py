o = input()

mat = [None] * 12
for linha in range(0, 12):
    mat[linha] = [None] * 12
    
for i in range(0, 12):
    for j in range(0, 12):
        mat[i][j] = float(input())
        
soma = 0
col = 11
for i in range(1,11):
    for j in range(col, 12): 
        soma += mat[i][j]
    if i < 5:
        col -= 1
    if i > 5:
        col += 1
        
qtde = (144 - 24) / 4        
if o == 'S':
    print("%.1f" % (soma))
else:
    print("%.1f" % (soma / qtde))
