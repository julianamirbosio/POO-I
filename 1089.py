while True:
    n = int(input())
    if n == 0:
        break
    
    magnitudes = list(map(int, input().split()))
    
    picos = 0 
    for i in range(n):
        if i == 0:
            if magnitudes[i] > magnitudes[n-1] and magnitudes[i] > magnitudes[i+1] or magnitudes[i] < magnitudes[n-1] and magnitudes[i] < magnitudes[i+1]:
                picos += 1
        elif i == n - 1:
            if magnitudes[i] > magnitudes[i-1] and magnitudes[i] > magnitudes[0] or magnitudes[i] < magnitudes[i-1] and magnitudes[i] < magnitudes[0]:
                picos += 1
        else:
            if magnitudes[i] > magnitudes[i-1] and magnitudes[i] > magnitudes[i+1] or  magnitudes[i] < magnitudes[i-1] and magnitudes[i] < magnitudes[i+1]:
                picos += 1
    
    print(picos)
