n = int(input())

casa_comprado = 0
casa_sobrando = 0
trab_comprado = 0
trab_sobrando = 0
    
for _ in range(n):
    sd, sn = input().split()
    
    if sd == "chuva" and casa_sobrando == 0:
        casa_comprado += 1
        trab_sobrando += 1
    elif sd == "chuva" and casa_sobrando > 0:
        casa_sobrando -= 1
        trab_sobrando += 1
        
    if sn == "chuva" and trab_sobrando == 0:
        trab_comprado += 1 
        casa_sobrando += 1 
    elif sn == "chuva" and trab_sobrando > 0:
        trab_sobrando -= 1 
        casa_sobrando += 1

print(casa_comprado, trab_comprado)
