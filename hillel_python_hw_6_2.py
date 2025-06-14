# Вводим данные
user_input = input("Введите количество секунд: ")

try:
    total_seconds = int(user_input)

    # Проверяем, что значение в пределах допустимого
    if total_seconds < 0 or total_seconds >= 8640000:
        print("Число должно быть от 0 до 8640000")
    else:
        # Считаем дни
        days = total_seconds // (24 * 60 * 60)
        remaining_seconds = total_seconds % (24 * 60 * 60)

        # Считаем часы
        hours = remaining_seconds // (60 * 60)
        remaining_seconds = remaining_seconds % (60 * 60)

        # Считаем минуты
        minutes = remaining_seconds // 60

        # Секунды
        seconds = remaining_seconds % 60

        # Обрабатываем слово "день" или "днів"
        if days == 1:
            day_word = "день"
        else:
            day_word = "днів"

        # Вывод с добавлением ведущих нулей
        print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

except ValueError:
    print("Ошибка! Нужно ввести целое число.")