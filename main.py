# def safe_divide(a, b, default):
#     return a / b if b != 0 else default

# print(safe_divide(10, 2, 0))       # 5.0
# print(safe_divide(10, 0, "ошибка"))  # ошибка

# # скобки → ** → * / // % → + - → сравнения → not → and → or
# print(2 + 3 * 4 ** 2)         # 50   (сначала 4**2=16, потом 3*16=48, потом 2+48)
# print((2 + 3) * 4 ** 2)       # 80   (скобки первыми)
# print(5 > 3 and 2 + 2 == 4)   # True (арифметика → сравнения → and)

# s1 = 'завтрак яичница'                     # одинарные кавычки
# s2 = "Парижский круассан готов :)! Ура!"   # двойные кавычки
# s3 = '1975'                                # это строка, а не число

# print(type(s3))       # <class 'str'>
# print(s3 + '1')       # 19751 (склейка строк)
# print(int(s3) + 1)    # 1976  (после преобразования в число)

# import math

# r = 5

# # Способ 1: по формуле pi * r^2
# area_formula = math.pi * r ** 2

# # Способ 2: численно — разбиваем круг на узкие вертикальные полоски.
# # Высота полоски в точке x равна 2*sqrt(r^2 - x^2), ширина dx.
# n = 100_000
# dx = 2 * r / n
# area_numeric = 0
# for i in range(n):
#     x = -r + (i + 0.5) * dx          # середина полоски
#     area_numeric += 2 * math.sqrt(r ** 2 - x ** 2) * dx

# print(f"По формуле: {area_formula:.5f}")   # 78.53982
# print(f"Численно:   {area_numeric:.5f}")   # ≈ 78.53982

# n = int(input("Введите число: "))
# print("Чётное" if n % 2 == 0 else "Нечётное")

# n = int(input("Введите число: "))
# if 10 <= n <= 20:
#     print("Число в диапазоне от 10 до 20")
# else:
#     print("Число вне диапазона")

# height = 1e2
# width = 1e1
# lenght = 1e3
# mass = 1e3
    
# def categorize_boxes(height = height, lenght = lenght, width = width, mass = mass):
#     volume = lenght * width * height
#     is_bulky = (
#         lenght >= 10_000
#         or width >= 10_000
#         or height >= 10_000
#         or volume >= 1_000_000_000
#     )
#     is_heavy = mass >= 100

#     if is_bulky and is_heavy:
#         return "Both"
#     elif is_bulky:
#         return "Bulky"
#     elif is_heavy:
#         return "Heavy"
#     else:
#         return "Neither"
     # Глобальная переменная

# def modify_global():
#     global x  # Объявляем, что будем работать с глобальной переменной x
#     x = 20    # Изменяем её значение

# modify_global()
# print(x)  # Выведет 20

s = [1, 23, 12, 123, 23, 123123, 3453, 3345, 353]

for i in range(len(s)):
    for j in range(i+1, len(s)):
        first = s[i]
        second = s[j]
        if first == second:
            print(first)
