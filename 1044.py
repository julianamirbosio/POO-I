A, B = input().split()
A = int(A)
B = int(B)
if A > B:
    R = A%B
    if R == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    R = B%A
    if R == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
