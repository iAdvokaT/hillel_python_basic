def some_gen(begin, end, func):
    """
    begin: перший елемент послідовності
    end: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    value = begin
    for _ in range(end):
        yield value
        value = func(value)

# Приклад
def pow(x):
    return x ** 2

# Перевірка
from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')