# Задача 1. Вывести числа от 1 до 10
# for i in range(1, 11):
#    print(i)

# Задача 2. Сумма чисел от 1 до 100

# sum=0
# for count  in range(101):
#    sum += count
# print(sum)

# Задача 3. Таблица умножения
# 5 Запроси число и выведи таблицу умножения от 1 до 10.
# digit = int(input("Введи число"))
# for i in range(11):
#     print(f"{i}*{digit} = {i*digit}")

# Задача 4. Факториал
# digit=int(input("Введи число"))
# result=1
# for i in range(1, digit+1):
#     result =result* i
# print(f"факториал {digit} = {result}")

# Задача 5. Игра «Угадай число» (полноценная версия)
secret = 42
#
while True:
    digit = int(input("угадай число: "))
    if digit > secret:
        print("твое число больше, пробуй еще")
    elif digit < secret:
        print("твое число меньше, пробуй еще")
    else:
        break
print("Ты угадал")
