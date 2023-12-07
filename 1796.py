Q = int(input())
n = input().split()

votos = 0
contra = 0

for i in range(len(n)):
    if n[i] == '0':
        votos += 1
    else:
        contra += 1
        
if (contra >= votos):
    print("N")
else:
    print("Y")
