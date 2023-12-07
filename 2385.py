n = int(input())
p, q, r, s, x, y = list(map(int, input().split()))
i, j = list(map(int, input().split()))

resultado = 0
for k in range(1,n+1):
    Aik = (p * i + q * k) % x
    Bkj = (r * k + s * j) % y
    resultado += Aik * Bkj

print(resultado)
