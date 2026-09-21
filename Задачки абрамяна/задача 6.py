a, b, c = map(float, input().split())
V = a * b * c
S = 2 * (a*b + b*c + a*c)
print(V, S)