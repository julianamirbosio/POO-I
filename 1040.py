A, B, C, D = input().split()
A = float(A)
B = float(B)
C = float(C)
D = float(D)
MEDIA = (A*2 + B*3 + C*4 + D)/10

print("Media: %.1f" % (MEDIA))
if (MEDIA>=7):
    print("Aluno aprovado.")
elif (MEDIA<5):
    print("Aluno reprovado.")
elif (6.9>=MEDIA>=5):
    print("Aluno em exame.")
    E = float(input())
    MEDIA1 = (MEDIA+E)/2
    print("Nota do exame: %.1f" % (E))
    if (MEDIA1>=5):
        print ("Aluno aprovado.")
    else:
        print ("Aluno reprovado.")
    print("Media final: %.1f" % (MEDIA1))
