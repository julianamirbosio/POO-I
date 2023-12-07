N = int(input())
A = N/365
X = N%365
M = X/30
D = X%30
print("%i ano(s)" % (A))
print("%i mes(es)" % (M))
print("%i dia(s)" % (D))
