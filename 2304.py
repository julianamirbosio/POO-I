I, N = list(map(int, input().split()))
saldo_d = saldo_e = saldo_f = I

for i in range(N):
    j = input().split()
    
    if j[0] == 'C':
        if j[1] == 'D':
            saldo_d -= int(j[2])
        elif j[1] == 'E':
            saldo_e -= int(j[2])
        else:
            saldo_f -= int(j[2])
            
    elif j[0] == 'V':
        if j[1] == 'D':
            saldo_d += int(j[2])
        elif j[1] == 'E':
            saldo_e += int(j[2])
        else:
            saldo_f += int(j[2])
    else:
        if j[1] == 'D':
            saldo_d += int(j[3])
            if j[2] == 'E':
                saldo_e -= int(j[3])
            elif j[2] == 'F':
                saldo_f -= int(j[3])
                
        elif j[1] == 'E':
            saldo_e += int(j[3])
            if j[2] == 'D':
                saldo_d -= int(j[3])
            elif j[2] == 'F':
                saldo_f -= int(j[3])
            
        else:
            saldo_f += int(j[3])
            if j[2] == 'D':
                saldo_d -= int(j[3])
            elif j[2] == 'E':
                saldo_e -= int(j[3])
                
print("%i %i %i" %(saldo_d, saldo_e, saldo_f))
