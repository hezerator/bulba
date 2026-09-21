x1, y1, x2, y2 = map(float, input().split())
side_a = abs(x2 - x1)
side_b = abs(y2 - y1)
P = 2 * (side_a + side_b)
S = side_a * side_b
print(P, S)