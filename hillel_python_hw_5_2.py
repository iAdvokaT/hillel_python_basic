print("Вітаю Вас у міні-калькуляторі \"Калькулятор на колінках\"")

while True:
    try:
        user_input = input("Введіть перше число або \"вихід\" для завершення: ").lower()
        if user_input == "вихід":
            print("Завершую програму! Дякую за використання.")
            break
        user_num1 = float(user_input)

        user_operation = input("Оберіть дію (+, -, *, /): ")
        if user_operation not in ["+", "-", "*", "/"]:
            print("Невідома операція. Спробуйте ще раз.")
            continue

        user_num2 = float(input("Введіть друге число: "))

        if user_operation == "+":
            result = user_num1 + user_num2
        elif user_operation == "-":
            result = user_num1 - user_num2
        elif user_operation == "*":
            result = user_num1 * user_num2
        elif user_operation == "/":
            if user_num2 == 0:
                print("На нуль ділити не можна.")
                continue
            result = user_num1 / user_num2

        print(f"Ось ваш результат: {result}")

        continue_choice = input("Бажаєте продовжити? (y/n): ").strip().lower()
        if continue_choice not in ["y", "yes"]:
            print("Завершую програму! Дякую за використання.")
            break

    except ValueError:
        print("Введено некоректне число. Спробуйте ще раз.")