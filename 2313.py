A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

if (A < B + C) and (B < A + C) and (C < A + B):
    if A == B == C:
        print("Valido-Equilatero")
    elif (A != B) and (A != C) and (B != C):
        print("Valido-Escaleno")
    else:
        print("Valido-Isoceles")
        
    if  (A**2 + B**2 == C**2) or (C**2 + A**2 == B**2) or (C**2 + B**2 == A**2): 
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else: 
    print("Invalido")
