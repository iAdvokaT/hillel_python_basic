def get_day_word(days):
    if 11 <= days % 100 <= 14:
        return "днів"
    last_digit = days % 10
    if last_digit == 1:
        return "день"
    elif 2 <= last_digit <= 4:
        return "дні"
    else:
        return "днів"

user_input = input("Введіть кількість секунд: ")

try:
    total_seconds = int(user_input)

    if not (0 <= total_seconds < 8640000):
        print("Число повинно бути від 0 до 8640000")
    else:
        days = total_seconds // 86400
        remaining = total_seconds % 86400

        hours = remaining // 3600
        remaining %= 3600

        minutes = remaining // 60
        seconds = remaining % 60

        day_word = get_day_word(days)

        # Вивід з нулями
        print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

except ValueError:
    print("Помилка! Введіть ціле число.")