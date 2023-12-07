n = int(input())
for _ in range(0,n):
    a,b = list(map(str, input().split()))
    if len(b) > len(a):
        print("nao encaixa")
    else:
        if a[len(a) - len(b): len(a)] == b:
            print("encaixa")
        else:
            print("nao encaixa")
