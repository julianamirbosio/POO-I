n = int(input())
for _ in range(0,n): #casos teste
    x = int(input())
    if x == 0:
        print("NULL")
    elif x % 2 == 0 and x > 0:
        print("EVEN POSITIVE")
    elif x % 2 == 0 and x < 0:
        print("EVEN NEGATIVE")
    elif x % 2 != 0 and x > 0:
        print("ODD POSITIVE")
    else:
        print("ODD NEGATIVE")
