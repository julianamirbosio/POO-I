n = int(input())
for _ in range(0,n):
    x,y = list(map(int, input().split()))
    r = (3*x)**2 + y**2
    b = 2*(x**2) + (5*y)**2
    c = -100*x + y**3
    if r > b and r > c:
        print("Rafael ganhou")
    elif b > r and b > c:
        print("Beto ganhou")
    elif c > r and c > b:
        print("Carlos ganhou")
