import math
a, b = map(float, input().split())
c = math.sqrt(a**2 + b**2)
P = a + b + c
print(c, P)