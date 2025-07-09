def common_elements():
    multiples_of_3 = {num for num in range(100) if num % 3 == 0}
    multiples_of_5 = {num for num in range(100) if num % 5 == 0}
    return multiples_of_3 & multiples_of_5

# Тест:
assert common_elements() == {0, 15, 30, 45, 60, 75, 90}, 'Test'
print('ОК')