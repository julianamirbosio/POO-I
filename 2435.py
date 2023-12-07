N1, D1, V1 = input().split()
N1 = int(N1)
D1 = int(D1)
V1 = int(V1)
N2, D2, V2 = input().split()
N2 = int(N2)
D2 = int(D2)
V2 = int(V2)

if (V1/D1) > (V2/D2):
    print(N1)
else:
    print(N2)
