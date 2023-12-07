n = int(input())
for _ in range(n):
    strings = input().split()
    strings = ' '.join(strings)
    cadeia = []
    str1, str2 = strings.split()
    
    i = 0
    j = 0
    
    while i < len(str1) and j < len(str2):
        cadeia.append(str1[i])
        cadeia.append(str2[j])
        i += 1
        j += 1
        
    while i < len(str1):
        cadeia.append(str1[i])
        i += 1
    
    while j < len(str2):
        cadeia.append(str2[j])
        j += 1
        
    cadeia = ''.join(cadeia)
    print(cadeia)
