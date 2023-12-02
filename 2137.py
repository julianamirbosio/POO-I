def ordem(livros):
    livros_ordenados = sorted(livros)
    return livros_ordenados
    
while True:
    try:
        biblioteca = []
        n = int(input())
        for _ in range(n):
            livro = input()
            biblioteca.append(livro)
        biblioteca_ordenada = ordem(biblioteca)
        for l in biblioteca_ordenada:
            print(l)
    except EOFError:
        break
