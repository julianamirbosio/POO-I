def verifica_linha_sudoku(tabela):
    for linha in tabela:
        numeros_na_linha = set(linha)            
        if numeros_na_linha != set(range(1, 10)):
            return False
    return True
    
def verifica_coluna_sudoku(tabela):
    transposta = list(zip(*tabela))
    for coluna in transposta:
        numeros_na_coluna = set(coluna)        
        if numeros_na_coluna != set(range(1, 10)):
            return False
    return True
    
def verifica_quadrado_sudoku(tabela):
    for i in range(0, 9, 3):  
        for j in range(0, 9, 3): 
            quadrado = []                
            for x in range(3):
                for y in range(3):
                    quadrado.append(tabela[i + x][j + y])                        
            if set(quadrado) != set(range(1, 10)):
                return False
    return True

w = int(input())
n = 1

for _ in range(w):
    
    sudoku = [None] * 9
    for i in range(9):
        sudoku[i] = list(map(int, input().split()))
            
    print("Instancia %i" %(n))
    n += 1
    
    if verifica_linha_sudoku(sudoku) and verifica_coluna_sudoku(sudoku) and verifica_quadrado_sudoku(sudoku):
        print("SIM")
    else:
        print("NAO")
        
    print()
