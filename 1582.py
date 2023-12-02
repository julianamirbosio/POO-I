def mdc(x, y):
    while y != 0:
        x, y = y, x % y
    return x
    
def mdc_tres_numeros(a, b, c):
    return mdc(mdc(a, b), c)  
    
def pit(a, b, c):
    pitty = sorted([a, b, c])
    cat1, cat2, hip = pitty
    return hip**2 == cat1**2 + cat2**2
    
while True:
    try:
        x, y, z = list(map(int, input().split()))
        if pit(x, y, z): 
            if mdc_tres_numeros(x, y, z) == 1:
                print("tripla pitagorica primitiva")
            else:
                print("tripla pitagorica")
        else:
            print("tripla")
    except EOFError:
        break
