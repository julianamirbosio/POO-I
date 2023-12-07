x = input().split()
y = input().split()
encaixa = True
for i in range(5):
    if x[i] == y[i]:
        encaixa = False
if encaixa:
    print('Y')
else:
    print('N')
