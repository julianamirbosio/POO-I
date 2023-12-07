quebrados = 0
n = int(input())
for _ in range(0,n):
    L, C = input().split()
    L = int(L)
    C = int(C)
    if L > C :
        quebrados += C
print(quebrados)
