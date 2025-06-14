import string
import keyword

var_name = input("Введіть ім'я змінної: ").strip()


def is_valid_variable(name):
    if name in keyword.kwlist:
        return False

    if name and name[0].isdigit():
        return False

    if any(ch.isupper() for ch in name):
        return False

    if " " in name:
        return False

    for ch in name:
        if ch in string.punctuation and ch != "_":
            return False

    if name.count('_') > 1 and len(name.strip('_')) == 0:
        return False


    if not name:
        return False

    return True


print(is_valid_variable(var_name))
