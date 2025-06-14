import string

alphabet = string.ascii_letters

user_input = input("Введіть дві літери через дефіс (наприклад, a-c): ")

start, end = user_input.split("-")

start_index = alphabet.index(start)
end_index = alphabet.index(end)

result = alphabet[start_index:end_index+1]

print(result)