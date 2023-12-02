def conversor(num):
    if len(num) >= 2 and num[1] == 'x':
        return int(num, 16)
    else:
        hexadecimal = hex(int(num)).upper()
        hexadecimal = hexadecimal[2:]
        return "0x" + hexadecimal
    
while True:
    try:
        num = input()
        if num[0] == '-':
            break
        else:
            print(conversor(num))
    except EOFError:
        break
