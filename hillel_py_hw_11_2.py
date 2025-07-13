def generate_cube_numbers(end):
    """Генерує куби чисел, починаючи з 2, поки куб не перевищить або не дорівнює end"""
    n = 2
    while True:
        cube = n ** 3
        if cube > end:
            return  # завершення генератора
        yield cube
        n += 1

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки 2^3 = 8, а 3^3 = 27 > 10'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5^3 = 125 > 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10^3 = 1000 — останнє включено'
print('OK')