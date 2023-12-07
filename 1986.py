n = int(input())
codigo = [int(x, 16) for x in input().split()]
mensagem = [chr(y) for y in codigo]
mensagem_str = ''.join(mensagem)
print(mensagem_str)
