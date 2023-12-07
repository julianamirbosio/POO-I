t = int(input())
for i in range(t):
    n, *equipe = map(int, input().split())
    equipe_ordenada = sorted(equipe)
    capitao = equipe_ordenada[len(equipe_ordenada) // 2]
    print("Case %i: %i" %(i+1, capitao))
