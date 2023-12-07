while True:
    d, n = input().split()   
    if d == '0' and n == '0':
        break
    n = [c for c in n if c != d]
    if not n:
        n = ['0']
    print(int(''.join(n)))
