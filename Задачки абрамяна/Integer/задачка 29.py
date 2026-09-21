A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
count = (A // C) * (B // C)
area_used = count * C * C
area_free = A * B - area_used
print("Количество квадратов:", count)
print("Площадь незанятой части:", area_free)