while True:
    try:
        A, B, C = list(map(int, input().split()))
        if A == B and B == C and A == C:
            print("*")
        elif A == B:
            print("C")
        elif A == C:
            print("B")
        elif B == C:
            print("A")
    except EOFError:
        break
