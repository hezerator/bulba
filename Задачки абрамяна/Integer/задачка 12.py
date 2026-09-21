n = int(input("Введите трёхзначное число: "))
hundreds = n // 100
tens = (n // 10) % 10
units = n % 10
reversed_num = units * 100 + tens * 10 + hundreds
print("Число справа налево:", reversed_num)