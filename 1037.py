V = float(input())
if 0 <= V <= 25:
    print("Intervalo [0,25]")
elif 25 < V <= 50:
    print("Intervalo (25,50]")
elif 50 < V <= 75:
    print("Intervalo [50,70]")
elif 75 < V <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
