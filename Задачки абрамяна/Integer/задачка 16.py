n = int(input("Введите трёхзначное число: "))
hundreds = n // 100
tens = (n // 10) % 10
units = n % 10
result = hundreds * 100 + units * 10 + tens
print("Полученное число:", result)