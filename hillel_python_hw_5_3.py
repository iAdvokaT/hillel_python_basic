import string

text = input("Введіть рядок для перетворення в хештег: ")

for symbol in string.punctuation:
    text = text.replace(symbol, "")

words = text.split()

capitalized_words = []
for word in words:
    capitalized_words.append(word.capitalize())

result = "#" + "".join(capitalized_words)

if len(result) > 140:
    result = result[:140]

print(result)