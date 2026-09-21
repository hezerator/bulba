n = int(input("Введите трёхзначное число: "))
hundreds = n // 100
tens = (n // 10) % 10
units = n % 10
print("Сумма цифр:", hundreds + tens + units)
print("Произведение цифр:", hundreds * tens * units)