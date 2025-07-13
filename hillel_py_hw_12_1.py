import re
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Выделяем все теги <...>
    cleaned_text = re.sub(r'<.*?>', '', html)

    # Розбиваем на рядкы и убираем пустые/беззмістовні
    lines = cleaned_text.split('\n')
    meaningful_lines = [line.strip() for line in lines if line.strip()]

    # Об'єднуємо знову в текст
    result = '\n'.join(meaningful_lines)

    # Записуємо в результатний файл
    with codecs.open(result_file, 'w', 'utf-8') as out_file:
        out_file.write(result)