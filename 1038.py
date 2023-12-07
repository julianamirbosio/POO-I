C, Q = input().split()
C = int(C)
Q = int(Q)

if (C == 1):
    T = Q * 4
elif (C == 2):
    T = Q * 4.5
elif (C == 3):
    T = Q * 5
elif (C == 4):
    T = Q * 2
elif (C == 5):
    T = Q * 1.5
print("Total: R$ %.2f" % (T))
