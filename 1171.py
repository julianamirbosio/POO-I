def num_frequencia(biblioteca):
    for num in sorted(biblioteca):
        print("%d aparece %d vez(es)" %(num, biblioteca[num]))
    
frequencia = {}
n = int(input())
for _ in range(n):
    num = int(input())
    if num in frequencia:
        frequencia[num] += 1
    else:
        frequencia[num] = 1
        
num_frequencia(frequencia)
