n = int(input("Введите трёхзначное число: "))
hundreds = n // 100
tens = (n // 10) % 10
units = n % 10
result = tens * 100 + units * 10 + hundreds
print("Полученное число:", result)