def correct_sentence(text):
    # Сделаем первую букву заглавной
    text = text[0].upper() + text[1:]

    # Проверим, есть ли точка в конце
    if not text.endswith('.'):
        text += '.'

    return text


# Тесты:
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')