# Просим пользователя ввести данные
num1 = float(input("Введите первое число: "))
operator = input("Введите знак (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

# Считаем результат
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "Ошибка: неверный знак"

print("Ответ:", result)