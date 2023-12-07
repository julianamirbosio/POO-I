N = int(input())
h = N/3600
x = N%3600
m = x/60
s = x%60
print("%i:%i:%i" % (h, m, s))
