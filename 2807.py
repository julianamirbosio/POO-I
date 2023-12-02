def iccanobif(n):
    if n <= 0:
        return []
        
    if n == 1:
        return [1]

    sequence = [1, 1]
    for _ in range(2, n):
        next_term = sequence[0] + sequence[1]
        sequence.insert(0, next_term)

    return sequence

n = int(input())
icc = " ".join(map(str, iccanobif(n)))
print(icc)
