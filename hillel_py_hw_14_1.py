# Кастомное исключение
class GroupFullException(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        self.message = message
        super().__init__(self.message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} років, {self.gender}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, залікова: {self.record_book}'


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullException(f"Не можна додати {student.first_name} {student.last_name} — група вже заповнена!")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(st) for st in self.group)
        return f'Номер групи: {self.number}\nСтуденти:\n{all_students}'

# Создаем группу
gr = Group("PD1")

# Добавляем 10 студентов
for i in range(1, 11):
    st = Student("Male", 20+i, f"Student{i}", f"Lastname{i}", f"ID{i}")
    gr.add_student(st)

# Пробуем добавить 11-го и ловим исключение
try:
    extra_student = Student("Female", 22, "Anna", "Ivanova", "ID999")
    gr.add_student(extra_student)
except GroupFullException as e:
    print("❗ Помилка:", e)

print()
print(gr)