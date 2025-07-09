def second_index(text, some_str):
    # поиск первое вхождение
    first = text.find(some_str)
    if first == -1:
        return None  # Если подстроки нет вовсе

    # поиск второе вхождение, начиная после первого
    second = text.find(some_str, first + 1)
    if second == -1:
        return None  # Если второго вхождения нет

    return second


# Тесты:
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')