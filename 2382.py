L, A, P, R = input().split()
L = float(L)
A = float(A)
P = float(P)
R = float(R)
diagonal = ((L**2) + (A**2) + (P**2))**0.5
diametro = 2*R
if diametro < diagonal:
    print("N")
else:
    print("S")
