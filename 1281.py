n = int(input())
for _ in range(n):
    
    feira = {}
    gasto = 0
    
    m = int(input())
    for _ in range(m):
        produto, preco = input().split()
        preco = float(preco)
        feira[produto] = preco
        
    p = int(input())
    for _ in range(p):
        compra, qnt = input().split()
        qnt = float(qnt)
        gasto += qnt * feira[compra]
        
    print("R$ %.2f" %(gasto))
