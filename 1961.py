P, N = list(map(int, input().split()))
sucesso = True

jogo = input().split()
for i in range(N):
    jogo[i] = int(jogo[i])

for i in range(len(jogo) - 1):
    if (jogo[i+1] - jogo[i] > P):
        sucesso = False
    elif (jogo[i] - jogo[i+1] > P):
        sucesso = False

if sucesso:
    print("YOU WIN")
else:
    print("GAME OVER")
