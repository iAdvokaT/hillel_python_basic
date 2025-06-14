user_input = input("Введите целое положительное число: ")

try:
    num = int(user_input)
    if num < 0:
        print("Введите положительное число!")
    elif num == 0:
        print(0)
    else:
        while num > 9:
            product = 1
            for digit in str(num):
                product *= int(digit)
            num = product
        print(f"Результат: {num}")
except ValueError:
    print("Ошибка! Нужно ввести целое целое число.")